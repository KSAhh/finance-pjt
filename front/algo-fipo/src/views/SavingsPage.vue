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
        <div class="flex-1 flex justify-center">
          <FilterSelector
            :filters="filters"
            :period-options="periodOptions"
            :product-types="productTypes"
            :selected-category="selectedCategory"
            :preferences="preferences"
            :selected-preferences="selectedPreferences"
            @update-filters="updateFilters"
            @update-preferences="updatePreferences"
          />
        </div>

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

      <!-- 기본 저축금리 정렬 -->

      <div class="flex space-x-4">
        <button
          @click="toggleSort('intr_rate')"
          class="py-2 px-4 bg-gray-100 border border-gray-300 rounded hover:bg-gray-200 flex items-center"
        >
          기본 저축금리순
          <span class="ml-2">{{ sortState.intr_rate === 'asc' ? '▲' : '▼' }}</span>
        </button>
        <button
          @click="toggleSort('intr_rate2')"
          class="py-2 px-4 bg-gray-100 border border-gray-300 rounded hover:bg-gray-200 flex items-center"
        >
          최고 우대금리순
          <span class="ml-2">{{ sortState.intr_rate2 === 'asc' ? '▲' : '▼' }}</span>
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
const currentPage = ref(1);
const itemsPerPage = 5;
// 은행 캐러셀 관련 선언
const bankNameStore = useBankNameStore();
const productStore = useProductStore();
const banks = computed(() => bankNameStore.banks);
const savingsBanks = computed(() => bankNameStore.savingsBanks);
const bankList = computed(() => bankNameStore.allBanks);


const sortState = ref({
  intr_rate: 'asc', // 기본 저축금리순
  intr_rate2: 'asc', // 최고 우대금리순
});



// 정렬 상태 토글
const toggleSort = (key) => {
  sortState.value[key] = sortState.value[key] === 'asc' ? 'desc' : 'asc';
  console.log(sortState.value[key])
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
  const sortKey = Object.keys(sortState.value).find((key) => sortState.value[key]);
  const sortOrder = sortState.value[sortKey];


  if (!sortKey) return currentProducts;

  return [...currentProducts].sort((a, b) => {
    if (sortOrder === 'asc') {
      return a[sortKey] - b[sortKey];
    } else {
      return b[sortKey] - a[sortKey];
    }
  });
});





  // console.log(sortedProducts)


const route = useRoute();
const router = useRouter();

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

const periodOptions = ["6개월", "12개월", "24개월"];

const filters = ref({ durations: [], types: [] });
const productTypes = {
  예금: ["특판", "방문없이가입", "누구나가입"],
  적금: [
    "특판",
    "방문없이가입",
    "청년적금",
    "군인적금",
    "주택청약",
    "자유적금",
    "정기적금",
    "청년도약계좌",
  ],
};
const preferences = ["비대면 가입", "은행 앱 사용", "급여 연동", "추천, 쿠폰"];
const selectedPreferences = ref([]);

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
  const typeFilters = filters.value.types.map((type) => `상품 유형: ${type}`);
  const preferenceFilters = selectedPreferences.value.map((pref) => `우대 조건: ${pref}`);

  return [...bankFilters, ...savingsBankFilters, ...durationFilters, ...typeFilters, ...preferenceFilters];
});

// 필터 업데이트 함수
const updateFilters = (newFilters) => {
  filters.value = newFilters;
};

// 우대 조건 업데이트 함수
const updatePreferences = (newPreferences) => {
  selectedPreferences.value = newPreferences;
};

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
  filters.value.types = filters.value.types.filter(
    (type) => `상품 유형: ${type}` !== filter
  );
  selectedPreferences.value = selectedPreferences.value.filter(
    (pref) => `우대 조건: ${pref}` !== filter
  );
  
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
  selectedPreferences: [],
  selectedBanks: [],
  showFilterModal: false,
};

const resetFilters = () => {
  Object.assign(filters.value, initialFilterState.filters);
  selectedPreferences.value = [...initialFilterState.selectedPreferences];
  selectedBanks.value = [...initialFilterState.selectedBanks];
  showFilterModal.value = initialFilterState.showFilterModal;
};

onMounted(() => {
  updateSelectedCategoryFromRoute();
  productStore.fetchProducts();
});
</script>

<style scoped>
</style>
