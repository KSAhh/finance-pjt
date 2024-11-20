<template>
    <div class="p-6 bg-gray-50 min-h-screen">
      <!-- 컨텐츠 전체를 감싸는 박스 -->
      <div class="max-w-5xl mx-auto bg-white rounded-lg shadow-lg p-6">
        <!-- 카테고리 선택 -->
        <CategorySelector
          :categories="categories"
          :selectedCategory="selectedCategory"
          @select-category="selectCategory"
        />
  
        <!-- 은행 캐러셀 -->
        <BankCarousel
          :banks="bankList"
          :selectedBanks="selectedBanks"
          @select-bank="toggleBank"
          class="mt-6"
        />
  
        <!-- 필터 버튼 -->
        <div class="mt-6 flex justify-end">
          <button
            @click="showFilterModal = true"
            class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition"
          >
            필터 설정
          </button>
        </div>
  
        <!-- 필터 모달 -->
        <FilterModal
          v-if="showFilterModal"
          :banks="banks"
          :savingsBanks="savingsBanks"
          :selectedBanks="selectedBanks"
          @update:selectedBanks="updateSelectedBanks"
          @close="showFilterModal = false"
        />
  
        <!-- 필터 선택 섹션 -->
        <FilterSelector
          :filters="filters"
          :productTypes="productTypes"
          :selectedCategory="selectedCategory"
          :selectedPreferences="selectedPreferences"
          @update-filters="updateFilters"
          @toggle-preferences="showPreferences = !showPreferences"
          class="mt-6"
        />
  
        <!-- 우대 조건 선택 모달 -->
        <PreferenceTable
          v-if="showPreferences"
          :preferences="preferences"
          :selectedPreferences="selectedPreferences"
          @update-preferences="updatePreferences"
        />
  
        <!-- 선택된 필터 표시 -->
        <SelectedFilters
          v-if="activeFiltersWithBanks.length > 0"
          :filters="activeFiltersWithBanks"
          @remove-filter="removeFilter"
          class="mt-4 border rounded-lg p-4 bg-gray-50"
        />
  
        <!-- 상품 리스트 -->
        <ProductList
          :products="filteredProducts"
          class="mt-6"
        />
  
        <!-- 필터 초기화 버튼 -->
        <div class="mt-6 flex justify-end">
          <button
            @click="resetFilters"
            class="px-6 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition"
          >
            필터 초기화
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from "vue";
  import { useRoute } from "vue-router";
  
  import CategorySelector from "@/components/Savings/SavingPage/CategorySelector.vue";
  import BankCarousel from "@/components/Savings/SavingPage/BankCarousel.vue";
  import FilterModal from "@/components/Savings/SavingPage/FilterModal.vue";
  import FilterSelector from "@/components/Savings/SavingPage/FilterSelector.vue";
  import PreferenceTable from "@/components/Savings/SavingPage/PreferenceTable.vue";
  import SelectedFilters from "@/components/Savings/SavingPage/SelectedFilters.vue";
  import ProductList from "@/components/Savings/SavingPage/ProductList.vue";
  
  import { banks, savingsBanks } from "@/data/bankData";
  
  const categories = ["예금", "적금"];
  const selectedCategory = ref(categories[0]);
  
  const route = useRoute();
  onMounted(() => {
    const queryCategory = route.query.category;
    if (categories.includes(queryCategory)) {
      selectedCategory.value = queryCategory;
    }
  });
  
  const bankList = ref([...banks, ...savingsBanks]); // 은행과 저축은행 합치기
  const selectedBanks = ref([]); // 선택된 은행 목록
  const showFilterModal = ref(false); // 필터 모달 상태
  
  const filters = ref({ duration: "", type: "" });
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
  const showPreferences = ref(false);
  
  const activeFilters = computed(() => {
    return [
      filters.value.duration && `기간: ${filters.value.duration}`,
      filters.value.type && `상품 유형: ${filters.value.type}`,
      ...selectedPreferences.value.map((pref) => `우대 조건: ${pref}`),
    ].filter(Boolean);
  });
  
  // 선택된 은행을 필터 목록에 추가
  const activeFiltersWithBanks = computed(() => {
    const bankFilters = [];
    if (selectedBanks.value.length === banks.length) {
      bankFilters.push("은행 전체");
    } else {
      const selectedBankNames = selectedBanks.value
        .filter((bankId) => banks.find((bank) => bank.id === bankId))
        .map((bankId) => banks.find((bank) => bank.id === bankId)?.name);
      bankFilters.push(...selectedBankNames);
    }
  
    if (selectedBanks.value.length === savingsBanks.length) {
      bankFilters.push("저축은행 전체");
    } else {
      const selectedSavingsBankNames = selectedBanks.value
        .filter((bankId) => savingsBanks.find((bank) => bank.id === bankId))
        .map((bankId) => savingsBanks.find((bank) => bank.id === bankId)?.name);
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
    showPreferences.value = false;
  };
  
  // 선택된 은행 업데이트 함수
  const updateSelectedBanks = (banks) => {
    selectedBanks.value = banks;
  };
  
  // 카테고리 선택 함수
  const selectCategory = (category) => {
    selectedCategory.value = category;
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
    if (`기간: ${filters.value.duration}` === filter) filters.value.duration = "";
    if (`상품 유형: ${filters.value.type}` === filter) filters.value.type = "";
    selectedPreferences.value = selectedPreferences.value.filter(
      (pref) => `우대 조건: ${pref}` !== filter
    );
  
    if (filter === "은행 전체") {
      selectedBanks.value = selectedBanks.value.filter(
        (bankId) => !banks.find((bank) => bank.id === bankId)
      );
    } else if (filter === "저축은행 전체") {
      selectedBanks.value = selectedBanks.value.filter(
        (bankId) => !savingsBanks.find((bank) => bank.id === bankId)
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
    filters.value = { duration: "", type: "" };
    selectedPreferences.value = [];
    selectedBanks.value = [];
  };
  </script>
  
  <style scoped>
  .p-6 {
    padding: 1.5rem;
  }
  
  .min-h-screen {
    min-height: 100vh;
  }
  
  .bg-gray-50 {
    background-color: #f9fafb;
  }
  
  .bg-white {
    background-color: #ffffff;
  }
  
  .rounded-lg {
    border-radius: 0.5rem;
  }
  
  .shadow-lg {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
      0 4px 6px -2px rgba(0, 0, 0, 0.05);
  }
  </style>
  