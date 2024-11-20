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

      <!-- 필터 버튼 -->
      <div class="mt-8 flex justify-end space-x-2">
        <button
          @click="showFilterModal = true"
          class="px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-300"
        >
          필터 설정
        </button>
        <button
          @click="resetFilters"
          class="px-3 py-2 bg-red-500 text-white font-semibold rounded-lg hover:bg-red-600 transition duration-300"
        >
          필터 초기화
        </button>
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

      <!-- 필터 선택 섹션 -->
      <FilterSelector
        :filters="filters"
        :period-options="periodOptions"
        :product-types="productTypes"
        :selected-category="selectedCategory"
        :preferences="preferences"
        :selected-preferences="selectedPreferences"
        @update-filters="updateFilters"
        @update-preferences="updatePreferences"
        class="mt-8"
      />

      <!-- 선택된 필터 표시 -->
      <SelectedFilters
        v-if="activeFiltersWithBanks.length > 0"
        :filters="activeFiltersWithBanks"
        @remove-filter="removeFilter"
        class="mt-6 border rounded-lg p-4 bg-gray-100"
      />

      <!-- 상품 리스트 -->
      <ProductList
        :products="filteredProducts"
        class="mt-8"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

import CategorySelector from "@/components/Savings/SavingPage/CategorySelector.vue";
import BankCarousel from "@/components/Savings/SavingPage/BankCarousel.vue";
import FilterModal from "@/components/Savings/SavingPage/FilterModal.vue";
import FilterSelector from "@/components/Savings/SavingPage/FilterSelector.vue";
import SelectedFilters from "@/components/Savings/SavingPage/SelectedFilters.vue";
import ProductList from "@/components/Savings/SavingPage/ProductList.vue";

import { banks as banksData, savingsBanks as savingsBanksData } from "@/data/bankData";

const categories = ["예금", "적금"];
const selectedCategory = ref(categories[0]);

const route = useRoute();
const router = useRouter();

// 쿼리 파라미터에 따라 selectedCategory 업데이트 함수
const updateSelectedCategoryFromRoute = () => {
  const queryCategory = route.query.category;
  if (categories.includes(queryCategory)) {
    selectedCategory.value = queryCategory;
  } else {
    selectedCategory.value = categories[0]; // 기본값 설정
  }
};

// 컴포넌트가 마운트될 때 초기화
onMounted(() => {
  updateSelectedCategoryFromRoute();
});

// 라우트의 쿼리 파라미터 변경 감시
watch(
  () => route.query.category,
  () => {
    updateSelectedCategoryFromRoute();
  }
);

const banks = ref(banksData);
const savingsBanks = ref(savingsBanksData);
const bankList = computed(() => [...banks.value, ...savingsBanks.value]);

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

const activeFilters = computed(() => {
  const durationFilters = filters.value.durations.map((duration) => `기간: ${duration}`);
  const typeFilters = filters.value.types.map((type) => `상품 유형: ${type}`);
  const preferenceFilters = selectedPreferences.value.map((pref) => `우대 조건: ${pref}`);
  return [...durationFilters, ...typeFilters, ...preferenceFilters];
});

// 선택된 은행을 필터 목록에 추가
const activeFiltersWithBanks = computed(() => {
  const bankFilters = [];

  // 은행 전체 선택 여부 확인
  const selectedBankIds = selectedBanks.value.filter((bankId) =>
    banks.value.some((bank) => bank.id === bankId)
  );
  if (selectedBankIds.length === banks.value.length && banks.value.length > 0) {
    bankFilters.push("은행 전체");
  } else {
    const selectedBankNames = selectedBankIds.map(
      (bankId) => banks.value.find((bank) => bank.id === bankId)?.name
    );
    bankFilters.push(...selectedBankNames);
  }

  // 저축은행 전체 선택 여부 확인
  const selectedSavingsBankIds = selectedBanks.value.filter((bankId) =>
    savingsBanks.value.some((bank) => bank.id === bankId)
  );
  if (
    selectedSavingsBankIds.length === savingsBanks.value.length &&
    savingsBanks.value.length > 0
  ) {
    bankFilters.push("저축은행 전체");
  } else {
    const selectedSavingsBankNames = selectedSavingsBankIds.map(
      (bankId) => savingsBanks.value.find((bank) => bank.id === bankId)?.name
    );
    bankFilters.push(...selectedSavingsBankNames);
  }

  return [...bankFilters, ...activeFilters.value];
});

const filteredProducts = ref([]);

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
};

// 카테고리 선택 함수
const selectCategory = (category) => {
  selectedCategory.value = category;
  // 선택한 카테고리를 쿼리 파라미터에 반영
  router.push({ query: { ...route.query, category } });
};

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

// 필터 초기화 함수
const resetFilters = () => {
  filters.value = { durations: [], types: [] };
  selectedPreferences.value = [];
  selectedBanks.value = [];
  showFilterModal.value = false;
};
</script>

<style scoped>
/* 스타일은 이전 답변과 동일하게 유지합니다. */
</style>
