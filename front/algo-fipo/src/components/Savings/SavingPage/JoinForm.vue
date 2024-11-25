<template>
  <div class="p-6">
    <h2 class="text-2xl font-bold mb-4">상품 가입</h2>

    <form @submit.prevent="submitForm" class="space-y-4">
      <!-- 상품 정보 -->
      <div>
        <label class="block text-sm font-medium">상품명</label>
        <input type="text" :value="form.fin_prdt_nm" readonly class="input bg-gray-100" />
      </div>

      <div>
        <label class="block text-sm font-medium">기관명</label>
        <input type="text" :value="form.kor_co_nm" readonly class="input bg-gray-100" />
      </div>

      <!-- 잔액 입력 -->
      <div>
        <label class="block text-sm font-medium">예치 금액 (원)</label>
        <input
          type="number"
          v-model.number="form.balance"
          class="input"
          min="0"
          placeholder="0"
        />
      </div>

      <!-- 시작일 -->
      <div>
        <label class="block text-sm font-medium">시작일</label>
        <input
          type="date"
          v-model="form.start_date"
          class="input"
          :max="today"
        />
      </div>

      <!-- 가입 기간 -->
      <div>
        <label class="block text-sm font-medium">가입 기간 (개월)</label>
        <select v-model="form.duration_months" class="input">
          <option v-for="month in durationOptions" :key="month" :value="month">
            {{ month }}개월
          </option>
        </select>
      </div>

      <!-- 제출 버튼 -->
      <div class="flex justify-end">
        <button
          type="submit"
          class="btn-submit"
          :disabled="form.balance <= 0"
        >
          제출
        </button>
      </div>
    </form>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const route = useRoute();
const router = useRouter();

const today = new Date().toISOString().split("T")[0];
const durationOptions = [1, 3, 6, 12, 24, 36];
const balanceError = ref("")

// 폼 데이터 초기화
const form = ref({
  product_type: route.query.product_type || "예금",
  balance: 0,
  start_date: today,
  duration_months: 36,
  product_pk: route.query.product_pk || "",
  kor_co_nm: route.query.kor_co_nm || "",
  fin_prdt_nm: route.query.fin_prdt_nm || "",
});

// 폼 제출
const API_URL = import.meta.env.VITE_API_BASE_URL

const submitForm = async () => {
  await axios.post(`${API_URL}/api/v1/products/user/`, form.value, {
    headers: {Authorization: `Token ${localStorage.getItem("key")}`}
  })
  .then((res) => {
    console.log("가입 성공:", res.data);
    alert("가입이 완료되었습니다");
    window.close(); // 창 닫기

  })
  .catch((err) => {
    console.log("가입 실패:", err)
    alert("가입에 실패했습니다.")
  })
}
</script>

<style scoped>
.input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn-submit {
  padding: 0.5rem 1rem;
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
const response = await axios.post(`${API_URL}/api/v1/products/user/`, form.value);
