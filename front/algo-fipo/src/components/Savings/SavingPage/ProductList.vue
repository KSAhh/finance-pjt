<template>
  <div>
    <h2 class="text-xl font-semibold mb-4">상품 리스트</h2>

    <!-- 로딩 상태 -->
    <div v-if="isLoading" class="text-center py-6">
      <p>상품 데이터를 불러오는 중입니다...</p>
    </div>

    <!-- 상품 데이터 -->
    <ul v-else-if="products && products.length > 0" class="space-y-4">
      <li
        v-for="product in paginatedProducts"
        :key="product.id"
        class="border border-gray-300 rounded-lg p-4 shadow-sm"
      >
        <h4 class="font-medium text-lg">{{ product.fin_prdt_nm }}</h4>
        <p class="text-sm text-gray-500">{{ product.kor_co_nm }}</p>
        <p class="text-sm mt-2">가입 방식: {{ formattedJoinWay(product.join_way) }}</p>
        <p class="text-sm">기본 금리: {{ product.options[0]?.intr_rate_type_nm }}</p>
        <p class="text-sm">저축 금리 유형명: {{ product.options[0]?.intr_rate }}</p>
        <p class="text-sm">최고 우대금리: {{ product.options[0]?.intr_rate2 }}</p>
        <p class="text-sm">저축 기간: {{ product.options[0]?.save_trm }}</p>
      </li>
    </ul>
    <!-- 데이터 없음 -->
    <p v-else class="text-center text-gray-500 py-6">조회된 상품이 없습니다.</p>

    <!-- 페이지네이션 -->
    <div class="flex items-center justify-center mt-6 space-x-4">
      <button @click="prevPage" :disabled="currentPage === 1" class="py-2 px-4 border border-gray-300 rounded bg-gray-100 hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed">이전</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages" class="py-2 px-4 border border-gray-300 rounded bg-gray-100 hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed">다음</button>
    </div>
  </div>
</template>

<script setup>
import { computed, defineProps, defineEmits, ref, watch } from 'vue';

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

const emit = defineEmits(['update:currentPage', 'sortRequested',]);


// // 필터 옵션 관리
// const saveTerms = ref([1, 3, 6, 12, 24, 36]);
// const selectedSaveTerms = ref([]);
// const joinWays = ref(['영업점', '인터넷', '스마트폰', '모집인', 'Unknown', '전화(텔레뱅킹)']);
// const selectedJoinWays = ref([]);
// const selectedInterestType = ref("");

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

// 현재 페이지 변경 시 부모에게 emit 처리 추가
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
// 부모로부터 전달된 products 데이터를 감시
watch(
  () => props.products,
  (newProducts) => {
    console.log('props.products 변경됨:', newProducts);
  },
  { immediate: true } // 컴포넌트가 로드될 때도 실행
);

// // 현재 페이지에 해당하는 상품 데이터 감시
// watch(
//   paginatedProducts,
//   (newPaginatedProducts) => {
//     console.log('paginatedProducts 변경됨:', newPaginatedProducts);
//   },
//   { immediate: true } // 컴포넌트가 로드될 때도 실행
// );
</script>

<style scoped>
/* 기존 스타일은 모두 TailwindCSS로 대체되었습니다. 필요에 따라 추가적인 TailwindCSS 커스터마이징을 할 수 있습니다. */
</style>
