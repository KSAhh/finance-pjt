<!-- src/components/loan/loanpage/OptionFilter.vue -->
<template>
    <div class="option-filter grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- 직군 필터 -->
      <div class="filter-section">
        <h3 class="text-lg font-semibold mb-2">직군 선택</h3>
        <div class="options flex flex-wrap gap-2">
          <label v-for="job in jobOptions" :key="job.id" class="flex items-center">
            <input
              type="checkbox"
              :value="job.id"
              v-model="selectedJobs"
              @change="onOptionFilterChanged"
              class="mr-2"
            />
            {{ job.name }}
          </label>
        </div>
        <div class="mt-2">
          <label class="flex items-center">
            <input
              type="checkbox"
              :checked="isAllJobsSelected"
              @change="toggleAllJobs"
              class="mr-2"
            />
            전체 선택
          </label>
        </div>
      </div>
  
      <!-- 대출종류 필터 -->
      <div class="filter-section">
        <h3 class="text-lg font-semibold mb-2">대출 종류</h3>
        <div class="options flex flex-wrap gap-2">
          <label v-for="type in loanTypes" :key="type.id" class="flex items-center">
            <input
              type="checkbox"
              :value="type.id"
              v-model="selectedLoanTypes"
              @change="onOptionFilterChanged"
              class="mr-2"
            />
            {{ type.name }}
          </label>
        </div>
        <div class="mt-2">
          <label class="flex items-center">
            <input
              type="checkbox"
              :checked="isAllLoanTypesSelected"
              @change="toggleAllLoanTypes"
              class="mr-2"
            />
            전체 선택
          </label>
        </div>
      </div>
  
      <!-- 금융권 필터 -->
      <div class="filter-section col-span-1 md:col-span-2 lg:col-span-3">
        <h3 class="text-lg font-semibold mb-2">금융권</h3>
        <div class="financial-groups flex flex-wrap gap-4">
          <div v-for="group in financialGroups" :key="group.id" class="financial-group w-full">
            <label class="flex items-center font-semibold">
              <input
                type="checkbox"
                :value="group.id"
                v-model="selectedFinancialGroups"
                @change="toggleFinancialGroup(group.id)"
                class="mr-2"
              />
              {{ group.name }}
            </label>
            <!-- 금융사 리스트 -->
            <div v-if="selectedFinancialGroups.includes(group.id)" class="financial-companies ml-4 mt-2">
              <label
                v-for="company in getCompaniesByGroup(group.id)"
                :key="company.id"
                class="flex items-center mr-4"
              >
                <input
                  type="checkbox"
                  :value="company.id"
                  v-model="selectedFinancialCompaniesLocal"
                  @change="onOptionFilterChanged"
                  class="mr-2"
                />
                {{ company.name }}
              </label>
            </div>
          </div>
        </div>
        <div class="mt-2">
          <label class="flex items-center">
            <input
              type="checkbox"
              :checked="isAllFinancialGroupsSelected"
              @change="toggleAllFinancialGroups"
              class="mr-2"
            />
            전체 선택
          </label>
        </div>
      </div>
  
      <!-- 특징 필터 -->
      <div class="filter-section col-span-1 md:col-span-2 lg:col-span-3">
        <h3 class="text-lg font-semibold mb-2">특징</h3>
        <div class="feature-buttons flex flex-wrap gap-2">
          <button
            v-for="feature in features"
            :key="feature.id"
            :class="[
              'px-4 py-2 rounded-full border',
              selectedFeatures.includes(feature.id)
                ? 'bg-green-500 text-white border-green-500'
                : 'bg-white text-gray-700 border-gray-300',
            ]"
            @click="toggleFeature(feature.id)"
          >
            {{ feature.name }}
          </button>
        </div>
        <div class="mt-2">
          <label class="flex items-center">
            <input
              type="checkbox"
              :checked="isAllFeaturesSelected"
              @change="toggleAllFeatures"
              class="mr-2"
            />
            전체 선택
          </label>
        </div>
      </div>
  
      <!-- 선택한 필터 표시 -->
      <div
        class="selected-filters mt-6 flex flex-wrap items-center gap-2"
        v-if="selectedFilterLabels.length > 0"
      >
        <span
          v-for="(label, index) in selectedFilterLabels"
          :key="index"
          class="filter-tag flex items-center bg-green-100 text-green-800 px-3 py-1 rounded-full"
        >
          {{ label }}
          <button @click="removeFilter(label)" class="ml-2 text-lg leading-none">&times;</button>
        </span>
        <button @click="resetFilters" class="ml-auto bg-red-500 text-white px-4 py-2 rounded">
          필터 초기화
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import {
    jobOptions,
    loanTypes,
    features,
    financialGroups,
    financialCompanySections,
    financialCompanies,
  } from '@/components/loan/loanpage/filterOptions.js'; // 공통 필터 옵션 모듈
  
  // Emits 정의
  const emit = defineEmits(['option-filter-changed']);
  
  // 선택된 필터 상태
  const selectedJobs = ref([]);
  const selectedLoanTypes = ref([]);
  const selectedFinancialGroups = ref([]);
  const selectedFinancialCompaniesLocal = ref([]);
  const selectedFeatures = ref([]);
  
  // 전체 선택 계산
  const isAllJobsSelected = computed(() => {
    return jobOptions.length > 0 && selectedJobs.value.length === jobOptions.length;
  });
  
  const isAllLoanTypesSelected = computed(() => {
    return loanTypes.length > 0 && selectedLoanTypes.value.length === loanTypes.length;
  });
  
  const isAllFinancialGroupsSelected = computed(() => {
    return (
      financialGroups.length > 0 &&
      selectedFinancialGroups.value.length === financialGroups.length
    );
  });
  
  const isAllFeaturesSelected = computed(() => {
    return features.length > 0 && selectedFeatures.value.length === features.length;
  });
  
  // 필터 변경 시 부모로 전달
  function onOptionFilterChanged() {
    emitOptionFilterChanged();
  }
  
  function emitOptionFilterChanged() {
    emit('option-filter-changed', {
      jobs: selectedJobs.value,
      loanTypes: selectedLoanTypes.value,
      financialGroups: selectedFinancialGroups.value,
      financialCompanies: selectedFinancialCompaniesLocal.value || [],
      features: selectedFeatures.value || [],
    });
  }
  
  // 전체 선택/해제 함수
  function toggleAllJobs() {
    if (isAllJobsSelected.value) {
      selectedJobs.value = [];
    } else {
      selectedJobs.value = jobOptions.map((job) => job.id);
    }
    onOptionFilterChanged();
  }
  
  function toggleAllLoanTypes() {
    if (isAllLoanTypesSelected.value) {
      selectedLoanTypes.value = [];
    } else {
      selectedLoanTypes.value = loanTypes.map((type) => type.id);
    }
    onOptionFilterChanged();
  }
  
  function toggleAllFinancialGroups() {
    if (isAllFinancialGroupsSelected.value) {
      selectedFinancialGroups.value = [];
      selectedFinancialCompaniesLocal.value = [];
    } else {
      selectedFinancialGroups.value = financialGroups.map((group) => group.id);
      selectedFinancialCompaniesLocal.value = financialCompanySections.flatMap(
        (section) => section.companies.map((company) => company.id)
      );
    }
    onOptionFilterChanged();
  }
  
  function toggleAllFeatures() {
    if (isAllFeaturesSelected.value) {
      selectedFeatures.value = [];
    } else {
      selectedFeatures.value = features.map((feature) => feature.id);
    }
    onOptionFilterChanged();
  }
  
  // 금융권 개별 선택 시
  function toggleFinancialGroup(groupId) {
    if (selectedFinancialGroups.value.includes(groupId)) {
      selectedFinancialGroups.value = selectedFinancialGroups.value.filter((id) => id !== groupId);
      // 해당 그룹의 모든 금융사 해제
      const section = financialCompanySections.find((sec) => sec.name === groupId);
      if (section) {
        const companyIds = section.companies.map((company) => company.id);
        selectedFinancialCompaniesLocal.value = selectedFinancialCompaniesLocal.value.filter(
          (id) => !companyIds.includes(id)
        );
      }
    } else {
      selectedFinancialGroups.value.push(groupId);
      // 해당 그룹의 모든 금융사 선택
      const section = financialCompanySections.find((sec) => sec.name === groupId);
      if (section) {
        const companyIds = section.companies.map((company) => company.id);
        selectedFinancialCompaniesLocal.value.push(
          ...companyIds.filter((id) => !selectedFinancialCompaniesLocal.value.includes(id))
        );
      }
    }
    onOptionFilterChanged();
  }
  
  // 금융사 리스트 가져오기
  function getCompaniesByGroup(groupId) {
    const section = financialCompanySections.find((sec) => sec.name === groupId);
    return section ? section.companies : [];
  }
  
  // 특징 필터 토글 함수
  function toggleFeature(featureId) {
    if (selectedFeatures.value.includes(featureId)) {
      selectedFeatures.value = selectedFeatures.value.filter((id) => id !== featureId);
    } else {
      selectedFeatures.value.push(featureId);
    }
    onOptionFilterChanged();
  }
  
  // 선택한 필터 라벨 생성
  const selectedFilterLabels = computed(() => {
    const labels = [];
  
    // 직군 선택 라벨
    if (selectedJobs.value.length > 0) {
      selectedJobs.value.forEach((jobId) => {
        const job = jobOptions.find((j) => j.id === jobId);
        if (job) labels.push(job.name);
      });
    }
  
    // 대출종류 선택 라벨
    if (selectedLoanTypes.value.length > 0) {
      selectedLoanTypes.value.forEach((typeId) => {
        const type = loanTypes.find((t) => t.id === typeId);
        if (type) labels.push(type.name);
      });
    }
  
    // 금융권 선택 라벨
    if (selectedFinancialGroups.value.length > 0) {
      selectedFinancialGroups.value.forEach((groupId) => {
        const group = financialGroups.find((g) => g.id === groupId);
        if (group) labels.push(group.name);
      });
    }
  
    // 금융사 선택 라벨
    if (selectedFinancialCompaniesLocal.value.length > 0) {
      selectedFinancialCompaniesLocal.value.forEach((companyId) => {
        const company = financialCompanies.find((c) => c.id === companyId);
        if (company) labels.push(company.name);
      });
    }
  
    // 특징 선택 라벨
    if (selectedFeatures.value.length > 0) {
      selectedFeatures.value.forEach((featureId) => {
        const feature = features.find((f) => f.id === featureId);
        if (feature) labels.push(feature.name);
      });
    }
  
    return labels;
  });
  
  // 필터 태그 제거 함수
  function removeFilter(label) {
    // 직군 필터 제거
    const job = jobOptions.find((j) => j.name === label);
    if (job) {
      selectedJobs.value = selectedJobs.value.filter((id) => id !== job.id);
      emitOptionFilterChanged();
      return;
    }
  
    // 대출종류 필터 제거
    const loanType = loanTypes.find((t) => t.name === label);
    if (loanType) {
      selectedLoanTypes.value = selectedLoanTypes.value.filter((id) => id !== loanType.id);
      emitOptionFilterChanged();
      return;
    }
  
    // 금융권 필터 제거
    const financialGroup = financialGroups.find((g) => g.name === label);
    if (financialGroup) {
      selectedFinancialGroups.value = selectedFinancialGroups.value.filter((id) => id !== financialGroup.id);
      // 해당 그룹의 모든 금융사 해제
      const section = financialCompanySections.find((sec) => sec.name === financialGroup.name);
      if (section) {
        const companyIds = section.companies.map((company) => company.id);
        selectedFinancialCompaniesLocal.value = selectedFinancialCompaniesLocal.value.filter(
          (id) => !companyIds.includes(id)
        );
      }
      emitOptionFilterChanged();
      return;
    }
  
    // 금융사 필터 제거
    const financialCompany = financialCompanies.find((c) => c.name === label);
    if (financialCompany) {
      selectedFinancialCompaniesLocal.value =
        selectedFinancialCompaniesLocal.value.filter((id) => id !== financialCompany.id);
      emitOptionFilterChanged();
      return;
    }
  
    // 특징 필터 제거
    const feature = features.find((f) => f.name === label);
    if (feature) {
      selectedFeatures.value = selectedFeatures.value.filter((id) => id !== feature.id);
      emitOptionFilterChanged();
      return;
    }
  }
  
  // 필터 초기화 함수
  function resetFilters() {
    selectedJobs.value = [];
    selectedLoanTypes.value = [];
    selectedFinancialGroups.value = [];
    selectedFinancialCompaniesLocal.value = [];
    selectedFeatures.value = [];
    emitOptionFilterChanged();
  }
  </script>
  
  <style scoped>
  .option-filter {
    /* 그리드 레이아웃 적용 */
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
  }
  
  .filter-section {
    display: flex;
    flex-direction: column;
  }
  
  .options,
  .financial-groups,
  .financial-companies,
  .feature-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  
  .financial-group {
    width: 100%;
  }
  
  .financial-companies {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  
  .selected-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  
  .filter-tag {
    display: flex;
    align-items: center;
  }
  
  .filter-tag button {
    background: none;
    border: none;
    margin-left: 5px;
    cursor: pointer;
  }
  
  .reset-button {
    background-color: #ff5c5c;
    color: #fff;
    padding: 5px 10px;
    border: none;
    border-radius: 15px;
    cursor: pointer;
  }
  
  .feature-section {
    /* 필요한 스타일 추가 */
  }
  
  .feature-buttons button {
    cursor: pointer;
  }
  </style>
  