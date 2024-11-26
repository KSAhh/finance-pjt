<template>
  <div>
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">상품 리스트</h2>

    <!-- 로딩 상태 -->
    <div v-if="isLoading" class="text-center py-6">
      <p class="text-lg text-gray-600">상품 데이터를 불러오는 중입니다...</p>
    </div>

    <!-- 상품 데이터 -->
    <ul v-else-if="products && products.length > 0" class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <li
        v-for="product in paginatedProducts"
        :key="product.id"
        class="border border-gray-200 rounded-lg p-6 shadow-md hover:shadow-lg hover:border-blue-400 transition duration-300 cursor-pointer"
        @click="goToDetail(product.id)"
      >
        <h4 class="font-medium text-lg text-blue-700 hover:text-blue-900 transition duration-200">
          {{ product.fin_prdt_nm }}
        </h4>
        <p class="text-sm text-gray-600">{{ product.kor_co_nm }}</p>
        <p class="text-sm mt-2">
          <span class="font-semibold text-gray-700">가입 방식:</span>
          {{ formattedJoinWay(product.join_way) }}
        </p>
        <p class="text-sm">
          <span class="font-semibold text-gray-700">저축 금리 유형:</span>
          {{ rateTypeSummary(product.options) }}
        </p>
        <p class="text-sm">
          <span class="font-semibold text-gray-700">기본 금리:</span>
          {{ product.options[0]?.intr_rate }}%
        </p>
        <p class="text-sm">
          <span class="font-semibold text-gray-700">최고 우대금리:</span>
          {{ maxInterestRate(product.options) }}%
        </p>
        <p class="text-sm">
          <span class="font-semibold text-gray-700">저축 기간:</span>
          {{ allSaveTerms(product.options) }}
        </p>
      </li>
    </ul>

    <!-- 데이터 없음 -->
    <p v-else class="text-center text-gray-500 py-6">
      조회된 상품이 없습니다.
    </p>

    <!-- 페이지네이션 -->
    <div class="flex items-center justify-center mt-8 space-x-4">
      <button
        @click="prevPage"
        :disabled="currentPage === 1"
        class="py-2 px-4 border border-gray-300 rounded bg-gray-100 hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed shadow-sm"
      >
        이전
      </button>
      <span class="font-medium text-gray-700">
        {{ currentPage }} / {{ totalPages }}
      </span>
      <button
        @click="nextPage"
        :disabled="currentPage === totalPages"
        class="py-2 px-4 border border-gray-300 rounded bg-gray-100 hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed shadow-sm"
      >
        다음
      </button>
    </div>
  </div>
</template>


<script setup>
import { computed, defineProps, defineEmits, ref, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
const router = useRouter()
const route = useRoute()

const props = defineProps({
  products: {
    type: Array,
    required: true,
    default: () => [],
  },
  isLoading: {
    type: Boolean,
    required: true,
  },
  currentPage: {
    type: Number,
    default: 1,
  },
  itemsPerPage: {
    type: Number,
    default: 5,
  },
});

watch(() => props.products, (newProducts) => {
  console.log("ProductList.vue의 products가 업데이트됨: ", newProducts);
});


const emit = defineEmits(['update:currentPage']);

const category = route.query.category

// 상세페이지 이동
const goToDetail = (id) => {
  router.push({ name: 'SavingsDetail', params: { id: id }, query: { category: category },})
}

// 총 페이지 수 계산
const totalPages = computed(() => {
  return props.products && props.products.length > 0 ? Math.ceil(props.products.length / props.itemsPerPage) : 1;
});

// 현재 페이지에 해당하는 상품들만 반환
const paginatedProducts = computed(() => {
  const start = (props.currentPage - 1) * props.itemsPerPage;
  const end = start + props.itemsPerPage;
  return props.products.slice(start, end);
});

// 이전 페이지로 이동
const prevPage = () => {
  if (props.currentPage > 1) {
    changePage(props.currentPage - 1);
  }
};

// 다음 페이지로 이동
const nextPage = () => {
  if (props.currentPage < totalPages.value) {
    changePage(props.currentPage + 1);
  }
};

// 현재 페이지 변경 시 부모에게 emit 처리
const changePage = (newPage) => {
  if (newPage > 0 && newPage <= totalPages.value) {
    emit('update:currentPage', newPage);
  }
};

// 가입방식 등 필터링된 데이터 포맷팅
const formattedJoinWay = (joinWay) => {
  if (!joinWay) return "정보 없음";
  if (Array.isArray(joinWay)) {
    return joinWay.join(", ");
  }
  try {
    const parsed = JSON.parse(joinWay.replace(/'/g, '"'));
    return Array.isArray(parsed) ? parsed.join(", ") : parsed;
  } catch (e) {
    console.error("join_way 파싱 실패:", joinWay, e);
    return joinWay;
  }
};

// 옵션에서 저축 금리 유형 요약
const rateTypeSummary = (options) => {
  const types = options.map((opt) => opt.intr_rate_type_nm).filter(Boolean);
  return [...new Set(types)].join(", "); // 중복 제거 후 문자열로 합침
};

// 옵션에서 최고 우대금리 계산
const maxInterestRate = (options) => {
  const rates = options.map((opt) => parseFloat(opt.intr_rate2 || "0"));
  return Math.max(...rates).toFixed(2); // 소수점 둘째 자리까지 반환
};

// 옵션에서 모든 저축 기간 표시
const allSaveTerms = (options) => {
  const terms = options.map((opt) => `${opt.save_trm}개월`).filter(Boolean);
  return [...new Set(terms)].join(", "); // 중복 제거 후 문자열로 합침
};

// 부모로부터 전달된 products 데이터를 감시
watch(
  () => props.products,
  (newProducts) => {
    console.log('props.products 변경됨: ', newProducts[0]);

  },
  { immediate: true }
);
</script>

<style scoped>
/* TailwindCSS 스타일로 기본 스타일 적용 */
</style>
