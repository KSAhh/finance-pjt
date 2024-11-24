<template>
    <h2 class="text-2xl font-bold mb-6">환율 계산기</h2>

    <!-- 기존 단위 선택 -->
    <label class="block mb-4">
      <span class="text-gray-700">기존 단위</span>
      <select v-model="fromCurrency" class="w-full border p-2 rounded">
        <option v-for="exchange in exchanges" :key="exchange.cur_unit" :value="exchange"
        :selected="exchange.cur_unit === 'KRW'">
          {{ exchange.cur_nm }} ({{ exchange.cur_unit }})
        </option>
      </select>
    </label>

    <!-- 바꿀 단위 선택 -->
    <label class="block mb-4">
      <span class="text-gray-700">바꿀 단위</span>
      <select v-model="toCurrency" class="w-full border p-2 rounded">
        <option v-for="exchange in exchanges"
          :key="exchange.cur_unit"
          :value="exchange"
          >
          {{ exchange.cur_nm }} ({{ exchange.cur_unit }})
        </option>
      </select>
    </label>

    <!-- 금액 입력 -->
    <label class="block mb-4">
      <span class="text-gray-700">금액</span>
      <input
        v-model.number="amount"
        type="number"
        class="w-full border p-2 rounded"
        placeholder="금액을 입력하세요"
      />
    </label>

    <!-- 결과 -->
    <div class="mt-6 p-4 rounded-lg border border-blue-300">
        <div class="result-container">
          <p ><span class="text-highlight">{{ formatNumber(amount) }}</span> {{ fromCurrency?.cur_unit }}</p>
          <p><i class="fa-solid fa-arrows-rotate"></i></p>
          <p><span class="text-highlight">{{ formatNumber(calculatedAmount) }}</span> {{ toCurrency?.cur_unit }}</p>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useExchangeStore } from "@/stores/exchangeStore";


// 상태 및 데이터
const store = useExchangeStore()
const fromCurrency = ref(null) // 기존 단위
const toCurrency = ref(null)   // 바꿀 단위
const amount = ref(0)          // 변환할 금액
const exchanges = computed(() => store.exchanges); // computed로 반응성 보장

// 데이터 가져오기
onMounted(async () => {
  
  await store.getExchangeRate()

  // 기본값 설정 (KRW로 초기화)
  const krwExchange = exchanges.value.find((exchange) => exchange.cur_unit === "KRW")
  const usdExchange = exchanges.value.find((exchange) => exchange.cur_unit === "USD")
  if (usdExchange) {
    toCurrency.value = krwExchange // 기본값을 USD로 설정
  if (krwExchange) {
    fromCurrency.value = usdExchange
  }
  }
})

// 계산된 금액
const calculatedAmount = computed(() => {
  if (!fromCurrency.value || !toCurrency.value || amount.value <= 0) {
    return 0;
  }

  if (fromCurrency.value.cur_unit === "KRW") {
    // KRW -> 외화
    return (amount.value * fromCurrency.value.krw_to_cur / 1000).toFixed(2);
  } else if (toCurrency.value.cur_unit === "KRW") {
    // 외화 -> KRW
    return (amount.value * fromCurrency.value.cur_to_krw).toFixed(2);
  } else {
    // 외화 -> 외화
    const krwAmount = amount.value * fromCurrency.value.cur_to_krw; // 외화 -> KRW
    return (krwAmount * toCurrency.value.krw_to_cur / 1000).toFixed(2);    // KRW -> 타 외화
  }
})

// 숫자 형식 변환 함수 (쉼표로 3자리씩 구분)
const formatNumber = (num) => {
  if (!num || isNaN(num)) return "0";
  return Number(num)
    .toLocaleString("en-US", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
      useGrouping: true,
    });
}


</script>

<style scoped>
/* TailwindCSS 스타일 적용 */
.result-container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: end; /* 세로 가운데 정렬 */
  gap: 1rem; /* 요소 간 간격 */
}
.result-container p {
  flex: 1; /* 양쪽 텍스트가 이모티콘과 동일한 비율로 간격을 유지 */
  text-align: center; /* 텍스트 가운데 정렬 */
}
.icon {
  font-size: 1.5rem;
  color: #163441; /* 이모티콘 색상 */
}

.text-highlight {
  color: #000000;
  font-weight: bold;
  font-size: 1.4rem;
}
</style>
