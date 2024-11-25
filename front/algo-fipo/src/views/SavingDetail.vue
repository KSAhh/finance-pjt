<template>
  <div>
    <div class="flex items-center justify-between mb-6">
      <!-- 제목 -->
      <h1 class="text-2xl font-bold">상품 상세 정보</h1>
      <!-- 가입하기 버튼 -->
      <button
        v-if="isLogin"
        @click="openJoinModal"
        class="btn-submit"
      >
        가입하기
      </button>
    </div>
    <div v-if="product">
        <JoinModal v-if="showJoinModal" 
          :product="product" 
          :category="category"
          @close="showJoinModal = false"
          />
    
    <!-- 기본 정보 -->
    <div class="border rounded-lg p-4 mb-6 shadow-sm">
        
        <p><strong>상품명:</strong> {{ product.fin_prdt_nm }}</p>
        <p><strong>기관명:</strong> {{ product.kor_co_nm }}</p>
        <p><strong>가입 방법:</strong> {{ formattedJoinWay(product.join_way) }}</p>
        <p><strong>만기 후 이자율 조건:</strong><br />
          <span v-html="formattedMtrtInt"></span>
        </p>
        <p><strong>우대 조건:</strong> {{ product.spcl_cnd }}</p>
        <p><strong>가입 제한:</strong> {{ joinDenyText(product.join_deny) }}</p>
        <p><strong>가입 대상:</strong> {{ product.join_member }}</p>
        <p><strong>최고 한도:</strong> {{ formatCurrency(product.max_limit) }}</p>
        <p><strong>기타 유의사항:</strong><br />
          <span v-html="formattedEtcNote"></span>
        </p>
        <p><strong>업데이트:</strong> {{ formatDate(product.fin_co_subm_day) }}</p>
    </div>

      <!-- 옵션 캐러셀 -->
    <h2 class="text-xl font-semibold mb-4">상품 옵션</h2>
    <div class="overflow-x-auto">
        <div class="flex space-x-4">
          <div
            v-for="(option, index) in product.options"
            :key="index"
            class="min-w-[200px] border p-4 rounded-lg shadow-sm flex-shrink-0"
          >
            <p><strong>저축 금리 유형:</strong> {{ option.intr_rate_type_nm }}</p>
            <p><strong>저축 기간:</strong> {{ option.save_trm }}개월</p>
            <p><strong>기본 금리:</strong> {{ option.intr_rate }}%</p>
            <p><strong>최고 우대금리:</strong> {{ option.intr_rate2 }}%</p>
            <p v-if="option.rsrv_type_nm && option.rsrv_type_nm !== 'Unknown'">
              <strong>적립 유형:</strong> {{ option.rsrv_type_nm }}
            </p>
          </div>
        </div>
    </div>
  </div>
  <!-- <div v-else>
    <p>상품 데이터를 불러오는 중입니다...</p>
  </div> -->


  <!-- 뒤로 가기 버튼 -->
  <button
    @click="goBack"
    class="mt-6 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 border"
  >
    목록으로 돌아가기
  </button>
  </div>
</template>
  
<script setup>
  import { ref, onMounted, onBeforeUnmount, computed } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useProductStore } from '@/stores/productStore'
  import { useNavBarStore } from '@/stores/navBarStore'
  import JoinForm from '@/components/Savings/SavingPage/JoinForm.vue'

  const isLogin = useNavBarStore().isLoggedIn
  // 가입 창
  const openJoinModal = () => {
    const query = new URLSearchParams({
      product_type: route.query.category === "예금" ? "예금" : "적금",
      product_pk: product.value.id,
      kor_co_nm: product.value.kor_co_nm,
      fin_prdt_nm: product.value.fin_prdt_nm,
    }).toString();

    const url = `/join?${query}`;
    window.open(url, "_blank", "width=600,height=700,scrollbars=yes");
  };
  
  const route = useRoute();
  const router = useRouter();
  const store = useProductStore()

  const productId = route.params.id;
  const product = ref(null);
  const category = route.query.category

  onMounted(async() => {
    // sessionStorage에서 데이터 가져오기
    const savedProduct = sessionStorage.getItem('product');

    if (savedProduct) {
        // 데이터가 이미 저장된 경우
        product.value = JSON.parse(savedProduct); // JSON 데이터 -> 자바스크립트 객체
        console.log('sessionStorage에서 불러온 상품:', product.value);
    } else {
        const products = route.query.category === '예금' ? store.products.deposits : store.products.savings;
        product.value = products.find((el) => String(el.id) === String(productId));

        if (product.value) {
            // sessionStorage에 데이터 저장
            sessionStorage.setItem('product', JSON.stringify(product.value));
            console.log('sessionStorage에 저장된 상품:', product.value);
        } else {
            console.error('상품을 찾을 수 없습니다.');
        }
    }
  })

  
  // 뒤로 가기 함수
  const goBack = () => {
    router.push({ path: '/saving', query: { category }}) // 쿼리 파라미터 유지
  }

  // 페이지 벗어날 때 sessionStorage 데이터 제거
    onBeforeUnmount(() => {
    sessionStorage.removeItem("product");
    console.log("sessionStorage product 데이터 삭제됨.");
    });

  
  // 가입 방식 포맷팅 함수
  const formattedJoinWay = (joinWay) => {
    if (!joinWay) return '정보 없음';
    if (Array.isArray(joinWay)) return joinWay.join(', ');
  
    try {
      const parsed = JSON.parse(joinWay.replace(/'/g, '"'));
      return Array.isArray(parsed) ? parsed.join(', ') : parsed;
    } catch (e) {
      console.error('join_way 파싱 실패:', joinWay, e);
      return joinWay;
    }
  };

  const joinDenyText = (joinDeny) => {
  if (joinDeny === 1) return '제한 없음';
  if (joinDeny === 2) return '서민 전용';
  if (joinDeny === 3) return '일부 제한';
  return '기관 문의';
};

  const formatDate = (dateString) => {
  if (!dateString || dateString === '000000000000') return '기관 문의';
  const year = dateString.slice(0, 4)
  const month = dateString.slice(4, 6)
  const day = dateString.slice(6, 8)
  return `${year}-${month}-${day}`
};

// 통화 형식으로 변환
const formatCurrency = (value) => {
    const numericValue = parseFloat(value);
    // 음수이거나 값이 없을 경우 "제한 없음" 반환
  if (numericValue < 0 || isNaN(numericValue)) {
    return "옵션별 상이";
  }
  return new Intl.NumberFormat('ko-KR', {
    style: 'currency',
    currency: 'KRW',
  }).format(value);
};

// \n을 <br>로 변환
const formattedMtrtInt = computed(() => {
    if (!product.value || !product.value.mtrt_int) {
    return "정보 없음"; // 기본값 설정
  }
  return product.value.mtrt_int.replace(/\n/g, "<br>");
})

// \n을 <br>로 변환
const formattedEtcNote = computed(() => {
  if (!product.value || !product.value.etc_note) {
    return "정보 없음"; // 기본값 설정
  }
  return product.value.etc_note.replace(/\n/g, "<br>");
})

// {
//     "id": 1,
//     "fin_prdt_cd": "WR0001B",
// },

  </script>
  <style scoped>
  .btn-submit {
  display: inline-block;
  background-color: #4caf50; /* 기본 배경색: 녹색 */
  color: white; /* 텍스트 색상 */
  font-size: 1.2rem; /* 글자 크기 */
  font-weight: bold; /* 글자 굵기 */
  padding: 0.8rem 1.6rem; /* 내부 여백 */
  border-radius: 8px; /* 둥근 모서리 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 약간의 그림자 */
  transition: all 0.3s ease; /* 호버 시 부드러운 애니메이션 */
  border: none;
  cursor: pointer;
}

.btn-submit:hover {
  background-color: #45a049; /* 호버 시 더 어두운 녹색 */
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15); /* 그림자 증가 */
  transform: translateY(-2px); /* 살짝 위로 이동하는 효과 */
}

.btn-submit:active {
  transform: translateY(0); /* 클릭 시 원래 위치로 돌아옴 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 클릭 시 그림자 원래대로 */
}
</style>
  