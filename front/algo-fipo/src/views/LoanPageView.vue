<!-- src/views/LoanPageView.vue -->
<template>
  <div class="bg-gray-50 min-h-screen flex flex-col items-center">
    <!-- 필터 섹션 -->
    <FilterSection
      class="w-full max-w-5xl bg-white rounded-lg shadow-lg p-8 mt-10"
      @filter-changed="onFilterChanged"
      :initial-category="initialCategory"
    />

    <!-- 상품 목록 -->
    <div class="w-full max-w-5xl mt-8">
      <LoanProductList :filters="selectedFilters" />
    </div>
  </div>
  </template>
  
  <script setup>
  import { ref, watch, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import FilterSection from '@/components/loan/loanpage/FilterSection.vue';
  import LoanProductList from '@/components/loan/loanpage/LoanProductList.vue';
  
  const route = useRoute();
  const router = useRouter();
  const selectedFilters = ref({});
  const initialCategory = ref(route.query.category || null);
  
  // 초기 필터 상태를 쿼리 파라미터에서 설정
  onMounted(() => {
    if (route.query) {
      selectedFilters.value = {
        jobs: route.query.jobs ? route.query.jobs.split(',') : [],
        loanTypes: route.query.loanTypes ? route.query.loanTypes.split(',') : [],
        features: route.query.features ? route.query.features.split(',') : [],
        financialGroups: route.query.financialGroups ? route.query.financialGroups.split(',') : [],
        financialCompanies: route.query.financialCompanies ? route.query.financialCompanies.split(',') : [],
        bank: route.query.bank || null,
      };
    }
  });
  
  // 라우트 변경 감지하여 초기 카테고리 업데이트
  watch(
    () => route.query.category,
    (newCategory) => {
      initialCategory.value = newCategory || null;
    }
  );
  
  // 필터 변경 시 처리 및 쿼리 파라미터 업데이트
  function onFilterChanged(filters) {
    selectedFilters.value = filters;
    // 쿼리 파라미터 업데이트
    const query = {};
    if (filters.jobs && filters.jobs.length > 0) {
      query.jobs = filters.jobs.join(',');
    }
    if (filters.loanTypes && filters.loanTypes.length > 0) {
      query.loanTypes = filters.loanTypes.join(',');
    }
    if (filters.features && filters.features.length > 0) {
      query.features = filters.features.join(',');
    }
    if (filters.financialGroups && filters.financialGroups.length > 0) {
      query.financialGroups = filters.financialGroups.join(',');
    }
    if (filters.financialCompanies && filters.financialCompanies.length > 0) {
      query.financialCompanies = filters.financialCompanies.join(',');
    }
    if (filters.bank) {
      query.bank = filters.bank;
    }
  
    router.replace({ path: route.path, query });
  }
  </script>
  
  <style scoped>

  </style>
  