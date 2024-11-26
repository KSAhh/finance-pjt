<template>
 <div class="max-w-5xl mx-auto p-6">
  <div class="max-w-5xl mx-auto p-6">
    <!-- 헤더 -->
    <div class="flex items-center justify-between mb-6">
      <h1 class="text-4xl font-bold text-gray-800 flex items-center space-x-3">
        <i class="fas fa-info-circle text-blue-600"></i>
        <span>상품 상세 정보</span>
      </h1>
      <!-- 가입하기 버튼 -->
      <button
        v-if="isLogin"
        @click="openJoinForm"
        class="btn-submit"
      >
        가입하기
      </button>
    </div>

    <!-- 기본 정보 -->
    <div v-if="product">
      <div class="border rounded-lg p-6 mb-8 shadow-lg bg-white">
        <h2 class="text-2xl font-semibold mb-6 text-gray-800 flex items-center space-x-3">
          <i class="fas fa-box-open text-red-500"></i>
          <span>기본 정보</span>
        </h2>
        <div class="grid grid-cols-2 gap-6">
          <p class="text-gray-700"><strong>상품명:</strong> {{ product.fin_prdt_nm }}</p>
          <p class="text-gray-700"><strong>기관명:</strong> {{ product.kor_co_nm }}</p>
          <p class="text-gray-700"><strong>가입 방법:</strong> {{ formattedJoinWay(product.join_way) }}</p>
          <p class="text-gray-700"><strong>만기 후 이자율 조건:</strong><br />
            <span v-html="formattedMtrtInt"></span>
          </p>
          <p class="text-gray-700"><strong>우대 조건:</strong> {{ product.spcl_cnd }}</p>
          <p class="text-gray-700"><strong>가입 제한:</strong> {{ joinDenyText(product.join_deny) }}</p>
          <p class="text-gray-700"><strong>가입 대상:</strong> {{ product.join_member }}</p>
          <p class="text-gray-700"><strong>최고 한도:</strong> {{ formatCurrency(product.max_limit) }}</p>
        </div>
        <div class="mt-4 border-t pt-4">
          <p class="text-gray-700"><strong>기타 유의사항:</strong><br />
            <span v-html="formattedEtcNote"></span>
          </p>
          <p class="text-gray-700 mt-2"><strong>업데이트:</strong> {{ formatDate(product.fin_co_subm_day) }}</p>
        </div>
      </div>

      <!-- 옵션 캐러셀 -->
      <div>
        <h2 class="text-2xl font-semibold mb-4 text-gray-800 flex items-center space-x-3">
          <i class="fas fa-list-alt text-yellow-600"></i>
          <span>상품 옵션</span>
        </h2>
        <div class="overflow-x-auto bg-white rounded-lg shadow-md p-4">
          <div class="flex space-x-4">
            <div
              v-for="(option, index) in product.options"
              :key="index"
              class="min-w-[220px] border border-gray-200 rounded-lg p-6 shadow-sm bg-gray-50"
            >
              <p class="text-gray-700"><strong>저축 금리 유형:</strong> {{ option.intr_rate_type_nm }}</p>
              <p class="text-gray-700"><strong>저축 기간:</strong> {{ option.save_trm }}개월</p>
              <p class="text-gray-700"><strong>기본 금리:</strong> <span style="color:red">{{ option.intr_rate }}%</span></p>
              <p class="text-gray-700"><strong>최고 우대금리:</strong> <span style="color:dodgerblue">{{ option.intr_rate2 }}%</span></p>
              <p v-if="option.rsrv_type_nm && option.rsrv_type_nm !== 'Unknown' && option.rsrv_type_nm !== '0.0'" class="text-gray-700">
                <strong>적립 유형:</strong> {{ option.rsrv_type_nm }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 뒤로가기 버튼 -->
    <button
      @click="goBack"
      class="mt-8 w-full md:w-auto px-6 py-3 bg-gray-900 text-white font-semibold rounded-lg hover:bg-gray-700 shadow-md transition duration-300"
    >
      목록으로 돌아가기
    </button>
  </div>

  </div>

</template>
  
<script setup>
  import { ref, onMounted, onBeforeUnmount, computed } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useProductStore } from '@/stores/productStore'
  import { useNavBarStore } from '@/stores/navBarStore'

  const isLogin = useNavBarStore().isLoggedIn
  // 가입 창
  const openJoinForm = () => {
    const query = new URLSearchParams({
      product_type: route.query.category === "예금" ? "예금" : "적금",
      product_pk: product.value.id,
      kor_co_nm: product.value.kor_co_nm,
      fin_prdt_nm: product.value.fin_prdt_nm,
      options: JSON.stringify(product.value.options), // JSON 문자열로 변환
    }).toString()

    const url = `/join?${query}`
    window.open(url, "_blank", "width=600,height=700,scrollbars=yes")
  }
  
  const route = useRoute()
  const router = useRouter()
  const store = useProductStore()

  const productId = route.params.id
  const product = ref(null);
  const category = route.query.category

  onMounted(async() => {
    // sessionStorage에서 데이터 가져오기
    const savedProduct = sessionStorage.getItem('product')

    if (savedProduct) {
        // 데이터가 이미 저장된 경우
        product.value = JSON.parse(savedProduct); // JSON 데이터 -> 자바스크립트 객체
        console.log('sessionStorage에서 불러온 상품:', product.value)
    } else {
        const products = route.query.category === '예금' ? store.products.deposits : store.products.savings;
        product.value = products.find((el) => String(el.id) === String(productId))

        if (product.value) {
            // sessionStorage에 데이터 저장
            sessionStorage.setItem('product', JSON.stringify(product.value))
            console.log('sessionStorage에 저장된 상품:', product.value)
        } else {
            console.error('상품을 찾을 수 없습니다.')
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
      console.log("sessionStorage product 데이터 삭제됨.")
    });

  
  // 가입 방식 포맷팅 함수
  const formattedJoinWay = (joinWay) => {
    if (!joinWay) return '정보 없음';
    if (Array.isArray(joinWay)) return joinWay.join(', ')
  
    try {
      const parsed = JSON.parse(joinWay.replace(/'/g, '"'))
      return Array.isArray(parsed) ? parsed.join(', ') : parsed
    } catch (e) {
      console.error('join_way 파싱 실패:', joinWay, e)
      return joinWay
    }
  };

  const joinDenyText = (joinDeny) => {
  if (joinDeny === 1) return '제한 없음'
  if (joinDeny === 2) return '서민 전용'
  if (joinDeny === 3) return '일부 제한'
  return '기관 문의';
};

  const formatDate = (dateString) => {
  if (!dateString || dateString === '000000000000') return '기관 문의'
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
    return "옵션별 상이"
  }
  return new Intl.NumberFormat('ko-KR', {
    style: 'currency',
    currency: 'KRW',
  }).format(value)
};

// \n을 <br>로 변환
const formattedMtrtInt = computed(() => {
    if (!product.value || !product.value.mtrt_int) {
    return "정보 없음"; // 기본값 설정
  }
  return product.value.mtrt_int.replace(/\n/g, "<br>")
})

// \n을 <br>로 변환
const formattedEtcNote = computed(() => {
  if (!product.value || !product.value.etc_note) {
    return "정보 없음"; // 기본값 설정
  }
  return product.value.etc_note.replace(/\n/g, "<br>")
})

  </script>
  <style scoped>
  .btn-submit {
  display: inline-block;
  background-color: #0048e8; 
  color: white; 
  font-size: 1.2rem;
  font-weight: bold;
  padding: 0.8rem 1.6rem; 
  border-radius: 8px; 
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
  transition: all 0.3s ease; 
  border: none;
  cursor: pointer;
}

.btn-submit:hover {
  background-color: white; 
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15); 
  transform: translateY(-2px); 
  color:black;
}

.btn-submit:active {
  transform: translateY(0); 
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
  