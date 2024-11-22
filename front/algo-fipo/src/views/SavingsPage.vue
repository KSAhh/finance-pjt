<template>
  <div class="bg-gray-50 min-h-screen">
    <!-- 컨텐츠 전체를 감싸는 박스 -->
    <div class="max-w-5xl mx-auto bg-white rounded-lg shadow-lg p-8 mt-10">
      <!-- 카테고리 선택 -->
      <CategorySelector
      :categories="categories"
      :selected-category="selectedCategory"
        @select-category="selectCategory"
      />
      
      
      <!-- 은행 캐러셀 -->
      <BankCarousel
      :banks="bankList"
      :selected-banks="selectedBanks"
      @select-bank="toggleBank"
      class="mt-8"
      />
      
      <!-- 버튼들과 필터 선택 섹션을 감싸는 컨테이너 -->
      <div class="mt-8 flex items-center justify-between">
        <!-- 왼쪽의 보이지 않는 요소 -->
        <div class="w-32"></div>
        
        <!-- 필터 선택 섹션 -->
        <div class="flex-1 flex justify-center whitespace-unwrap">
          <FilterSelector
          :filters="filters"
          :period-options="periodOptions"
    :product-types="productTypes"
    :selected-category="selectedCategory"
    :interest-rate-types="interestRateTypes"
    :join-methods="joinMethods"
    @update-filters="updateFilters"
    @update-preferences="updatePreferences"
    />
  </div>
  <!-- :preferences="preferences"
  :selected-preferences="selectedPreferences" (위 필터섹션에서 제외)--> 

  
  <!-- 필터 버튼 -->
  <div class="flex flex-col items-end space-y-2">
          <button
            @click="showFilterModal = true"
            class="px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-300"
          >
            필터 설정
          </button>
          <button
            @click="resetFilters"
            class="px-6 py-3 bg-red-600 text-white font-semibold rounded-lg hover:bg-red-700 transition duration-300"
          >
            필터 초기화
          </button>
        </div>
      </div>

      <!-- 필터 모달 -->
      <FilterModal
        v-if="showFilterModal"
        :banks="banks"
        :savings-banks="savingsBanks"
        :selected-banks="selectedBanks"
        @update:selected-banks="updateSelectedBanks"
        @close="showFilterModal = false"
      />

      <!-- 선택된 필터 표시 -->
      <SelectedFilters
        v-if="activeFiltersWithBanks.length > 0"
        :filters="activeFiltersWithBanks"
        @remove-filter="removeFilter"
        class="mt-6 border rounded-lg p-4 bg-gray-100"
      />
    <!-- 필터 및 정렬 옵션 버튼 -->

    <div class="flex space-x-4">
  <!-- 기본 저축금리순 -->
  <button
    @click="toggleSort('intr_rate')"
    class="py-2 px-4 bg-gray-100 border border-gray-300 rounded hover:bg-gray-200 flex items-center"
  >
    기본 저축금리순
    <span class="ml-2">
      {{ sortState.intr_rate === 'desc' ? '▼' : '▲' }}
    </span>
  </button>

  <!-- 최고 우대금리순 -->
  <button
    @click="toggleSort('intr_rate2')"
    class="py-2 px-4 bg-gray-100 border border-gray-300 rounded hover:bg-gray-200 flex items-center"
  >
    최고 우대금리순
    <span class="ml-2">
      {{ sortState.intr_rate2 === 'asc' ? '▲' : sortState.intr_rate2 === 'desc' ? '▼' : '▲' }}
    </span>
  </button>
</div>


      <!-- 상품 리스트 -->
      <ProductList
    :products="sortedProducts"
    :isLoading="productStore.isLoading"
    v-model:currentPage="currentPage"
    :itemsPerPage="itemsPerPage"
    
  />
    </div>
  </div>
</template>
<!-- @sortRequested="handleSortRequested" -->
<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import CategorySelector from "@/components/Savings/SavingPage/CategorySelector.vue";
import BankCarousel from "@/components/Savings/SavingPage/BankCarousel.vue";
import FilterModal from "@/components/Savings/SavingPage/FilterModal.vue";
import FilterSelector from "@/components/Savings/SavingPage/FilterSelector.vue";
import SelectedFilters from "@/components/Savings/SavingPage/SelectedFilters.vue";
import ProductList from "@/components/Savings/SavingPage/ProductList.vue";
import { useProductStore } from "@/stores/productstore";
import { useBankNameStore } from "@/stores/banknamestore";
const route = useRoute();
const router = useRouter();
const currentPage = ref(1);
const itemsPerPage = 5;
// 은행 캐러셀 관련 선언
const bankNameStore = useBankNameStore();
const productStore = useProductStore();
const banks = computed(() => bankNameStore.banks);
const savingsBanks = computed(() => bankNameStore.savingsBanks);
const bankList = computed(() => bankNameStore.allBanks);
// 단리/복리 선택 옵션
const interestRateTypes = ["단리", "복리"];

// 가입 방법 옵션
const joinMethods = ["영업점", "인터넷", "스마트폰", "전화(텔레뱅킹)", "Unknown"];


const sortState = ref({
  intr_rate: 'asc', // 기본값: 기본 저축금리순 오름차순
  intr_rate2: null, // 최고 우대금리순: 선택되지 않음
});



const toggleSort = (key) => {
  // 1. 다른 키는 초기화
  Object.keys(sortState.value).forEach((k) => {
    if (k !== key) sortState.value[k] = null; // 현재 클릭된 키 외의 정렬 상태 초기화
  });

  // 2. 현재 클릭된 키의 정렬 상태를 토글
  sortState.value[key] = sortState.value[key] === "asc" ? "desc" : "asc";

  console.log("현재 정렬 상태:", sortState.value); // 디버깅 로그
};







const selectCategory = (category) => {
  console.log("선택된 카테고리:", category); // 콘솔에 로그 출력
  selectedCategory.value = category;
  // 선택한 카테고리를 쿼리 파라미터에 반영
  
  router.push({ query: { ...route.query, category } });
};
const categories = ["예금", "적금"];
const selectedCategory = ref(categories[0]);

// 선택된 카테고리에 따른 상품 필터링
const filteredProductsByCategory = computed(() => {
  if (selectedCategory.value === "예금") {
    return productStore.products.deposits || [];
  } else if (selectedCategory.value === "적금") {
    return productStore.products.savings || [];
  }
  console.log(filteredProductsByCategory.value)
  return [];
});


const sortedProducts = computed(() => {
  const currentProducts = filteredProductsByCategory.value;

  // 활성화된 정렬 키와 방향 가져오기 (기본값: intr_rate, asc)
  const sortKey = Object.keys(sortState.value).find((key) => sortState.value[key]) || "intr_rate";
  const sortOrder = sortState.value[sortKey] || "asc";

  // 1. 필터링
  const filteredProducts = currentProducts.filter((product) => {
  
  // 은행 이름 필터링
  const bankMatch =
  selectedBanks.value.length === 0 || // 은행 필터가 없거나
  selectedBanks.value.some((selectedBankId) => {
    const bankData = [...banks.value, ...savingsBanks.value];
    const selectedBank = bankData.find((bank) => bank.id === selectedBankId);
    return selectedBank && product.kor_co_nm.includes(selectedBank.name); // 포함 관계 확인
  });
  
    // 기간 필터링
  const durationMatch = 
    filters.value.durations.length === 0 || // 필터가 없거나
    product.options.some((option) =>
      filters.value.durations.includes(String(option.save_trm)) // save_trm이 필터 조건에 포함
    );

  // 단리/복리 필터링
  const rateTypeMatch =
    filters.value.interestRateTypes.length === 0 || // 필터가 없거나
    product.options.some((option) =>
      filters.value.interestRateTypes.includes(option.intr_rate_type_nm) // intr_rate_type_nm이 필터 조건에 포함
    );

  // 가입 방법 필터링
  const joinWayMatch =
    filters.value.joinMethods.length === 0 || // 필터가 없거나
    filters.value.joinMethods.some((method) => 
      product.join_way.includes(method) // join_way 배열 중 하나라도 조건에 포함
    );

  // 최종 매칭 결과
  return bankMatch && durationMatch && rateTypeMatch && joinWayMatch;
  });


  // 2. 정렬
  return [...filteredProducts].sort((a, b) => {
    // 각 상품의 options 배열에서 정렬 기준 값 추출
    const aMaxRate = Math.max(
      ...a.options.map((option) => parseFloat(option[sortKey] || "0")) // 문자열을 숫자로 변환
    );
    const bMaxRate = Math.max(
      ...b.options.map((option) => parseFloat(option[sortKey] || "0")) // 문자열을 숫자로 변환
    );

    // 숫자로 정렬
    return sortOrder === "asc" ? aMaxRate - bMaxRate : bMaxRate - aMaxRate;
  });
});


// 쿼리 파라미터에 따라 selectedCategory 업데이트 함수
const updateSelectedCategoryFromRoute = () => {
  const queryCategory = route.query.category;

  if (categories.includes(queryCategory)) {
    selectedCategory.value = queryCategory;
    console.log("selectedCategory 업데이트됨:", selectedCategory.value);
  } else {
    selectedCategory.value = categories[0];
    console.log("유효하지 않은 카테고리, 기본값 설정:", selectedCategory.value);
  }
};

// 라우트의 쿼리 파라미터 변경 감시
watch(
  () => route.query.category,
  (newCategory, oldCategory) => {
    console.log("쿼리 파라미터 변경:", { newCategory, oldCategory });
    updateSelectedCategoryFromRoute();
  }
);

watch(filteredProductsByCategory, (newVal) => {
  console.log("필터링된 상품 리스트 업데이트:", newVal);
});

const selectedBanks = ref([]); // 선택된 은행 목록
const showFilterModal = ref(false); // 필터 모달 상태

const periodOptions = ["1", "3", "6", "12", "24", "36"];

const filters = ref({
  durations: [], // 기간 필터
  // types: [], // 상품 유형 필터
  interestRateTypes: [], // 단리/복리 필터
  joinMethods: [], // 가입 방법 필터
});

// const productTypes = {
//   예금: ["특판", "방문없이가입", "누구나가입"],
//   적금: [
//     "특판",
//     "방문없이가입",
//     "청년적금",
//     "군인적금",
//     "주택청약",
//     "자유적금",
//     "정기적금",
//     "청년도약계좌",
//   ],
// };
// const preferences = ["비대면 가입", "은행 앱 사용", "급여 연동", "추천, 쿠폰"];
// const selectedPreferences = ref([]);우대조건

const generateBankFilters = (bankList, selectedBankIds, label) => {
  if (selectedBankIds.length === bankList.length && bankList.length > 0) {
    return [label];
  }
  return selectedBankIds
    .map((bankId) => bankList.find((bank) => bank.id === bankId)?.name)
    .filter(Boolean);
};

const activeFiltersWithBanks = computed(() => {
  const bankFilters = generateBankFilters(banks.value, selectedBanks.value, "은행 전체");
  const savingsBankFilters = generateBankFilters(
    savingsBanks.value,
    selectedBanks.value,
    "저축은행 전체"
  );

  const durationFilters = filters.value.durations.map((duration) => `기간: ${duration}`);
  // const typeFilters = filters.value.types.map((type) => `상품 유형: ${type}`);
  // const preferenceFilters = selectedPreferences.value.map((pref) => `우대 조건: ${pref}`);



  return [...bankFilters, ...savingsBankFilters, ...durationFilters];
});
// ...preferenceFilters(위 리턴에서 제외)...typeFilters,
const updateFilters = (newFilters) => {
  filters.value = {
    ...filters.value,
    durations: newFilters.durations || [],
    types: newFilters.types || [],
    interestRateTypes: newFilters.interestRateTypes || [],
    joinMethods: newFilters.joinMethods || [],
  };
};



// 우대 조건 업데이트 함수
// const updatePreferences = (newPreferences) => {
//   selectedPreferences.value = newPreferences;
// };

// 선택된 은행 업데이트 함수
const updateSelectedBanks = (banks) => {
  selectedBanks.value = banks;
}

// 은행 선택 토글 함수
const toggleBank = (bank) => {
  if (selectedBanks.value.includes(bank.id)) {
    selectedBanks.value = selectedBanks.value.filter((b) => b !== bank.id);
  } else {
    selectedBanks.value.push(bank.id);
  }
};

// 필터 제거 함수
const removeFilter = (filter) => {
  filters.value.durations = filters.value.durations.filter(
    (duration) => `기간: ${duration}` !== filter
  );
  // filters.value.types = filters.value.types.filter(
  //   (type) => `상품 유형: ${type}` !== filter
  // );
  // selectedPreferences.value = selectedPreferences.value.filter(
  //   (pref) => `우대 조건: ${pref}` !== filter
  // );
  
  if (filter === "은행 전체") {
    selectedBanks.value = selectedBanks.value.filter(
      (bankId) => !banks.value.some((bank) => bank.id === bankId)
    );
  } else if (filter === "저축은행 전체") {
    selectedBanks.value = selectedBanks.value.filter(
      (bankId) => !savingsBanks.value.some((bank) => bank.id === bankId)
    );
  } else {
    selectedBanks.value = selectedBanks.value.filter((bankId) => {
      const bankName =
      bankList.value.find((bank) => bank.id === bankId)?.name || bankId;
      return bankName !== filter;
    });
  }
};

const initialFilterState = {
  filters: { durations: [], types: [] },
  // selectedPreferences: [],
  selectedBanks: [],
  showFilterModal: false,
};

const resetFilters = () => {
  Object.assign(filters.value, initialFilterState.filters);
  selectedBanks.value = [...initialFilterState.selectedBanks];
  showFilterModal.value = initialFilterState.showFilterModal;
};
// selectedPreferences.value = [...initialFilterState.selectedPreferences];


// const resetFilters = () => {
//   Object.assign(filters.value, initialFilterState.filters);
//   selectedBanks.value = []; // 은행 선택 초기화
//   showFilterModal.value = initialFilterState.showFilterModal;
// };

onMounted(() => {
  updateSelectedCategoryFromRoute();
  productStore.fetchProducts();
});
</script>

<style scoped>
</style>
