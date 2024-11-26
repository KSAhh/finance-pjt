<!-- src/components/loan/loanpage/FilterSection.vue -->
<template>
    <section class="filter-section p-4 bg-white shadow rounded-lg mb-6">
      <!-- 옵션 필터 -->
      <OptionFilter
        @option-filter-changed="onOptionFilterChanged"
        :initial-category="initialCategory"
      />
  
      <!-- 은행 필터 캐러셀 -->
      <BankFilterCarousel @bank-filter-changed="onBankFilterChanged" />
  
      <!-- 특징 필터 등 다른 필터 섹션 -->
      <!-- Optionally, add more filter components here -->
    </section>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import OptionFilter from '@/components/loan/loanpage/OptionFilter.vue';
  import BankFilterCarousel from '@/components/loan/loanpage/BankFilterCarousel.vue';
  
  // Props 정의
  const props = defineProps({
    initialCategory: {
      type: String,
      default: null,
    },
  });
  
  // Emits 정의
  const emit = defineEmits(['filter-changed']);
  
  // 필터 상태
  const selectedBank = ref(null);
  const selectedOptions = ref({
    jobs: [],
    loanTypes: [],
    features: [],
    financialGroups: [],
    financialCompanies: [],
  });
  
  // 필터 변경 시 처리 및 상태 업데이트
  function onOptionFilterChanged(filters) {
    selectedOptions.value = { ...selectedOptions.value, ...filters };
    emitFilters();
  }
  
  function onBankFilterChanged(bankId) {
    selectedBank.value = bankId;
    emitFilters();
  }
  
  // 필터 상태를 부모로 전달
  function emitFilters() {
    emit('filter-changed', { ...selectedOptions.value, bank: selectedBank.value });
  }
  </script>
  
  <style scoped>
  /* .filter-section {
    margin-bottom: 20px;
  } */

  /* 기본 레이아웃 스타일 */
  /* .bg-gray-50 {
    background-color: #f9fafb;
  }

  .max-w-5xl {
    max-width: 80rem;
  }

  .shadow-lg {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .mt-10 {
    margin-top: 2.5rem;
  }

  .mt-8 {
    margin-top: 2rem;
  } */

</style>
  