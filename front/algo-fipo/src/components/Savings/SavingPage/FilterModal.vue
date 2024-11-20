<template>
    <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div class="bg-white rounded-lg shadow-lg w-3/4 h-3/4 overflow-y-auto p-6">
        <!-- 모달 헤더 -->
        <div class="flex justify-between items-center pb-4 border-b border-gray-300">
          <h2 class="text-lg font-semibold">은행 및 저축은행 선택</h2>
          <button @click="$emit('close')" class="text-gray-600 hover:text-black">✕</button>
        </div>
  
        <!-- 은행 목록 섹션 -->
        <section class="mt-4">
          <div class="flex items-center mb-2">
            <h3 class="text-lg font-semibold">은행</h3>
            <button
              @click="toggleSelectAllBanks"
              class="ml-4 px-2 py-1 text-sm border rounded"
            >
              {{ isAllBanksSelected ? '전체 해제' : '전체 선택' }}
            </button>
          </div>
          <div class="grid grid-cols-4 gap-4 mt-2">
            <div
              v-for="bank in banks"
              :key="bank.id"
              class="flex items-center gap-2 p-2 border rounded hover:bg-gray-100 cursor-pointer"
              @click="toggleSelection(bank)"
              :class="{ 'bg-blue-100': isSelected(bank) }"
            >
              <img :src="bank.logo || '/default-logo.png'" alt="Bank Logo" class="w-8 h-8" />
              <span>{{ bank.name }}</span>
            </div>
          </div>
        </section>
  
        <!-- 저축은행 목록 섹션 -->
        <section class="mt-6">
          <div class="flex items-center mb-2">
            <h3 class="text-lg font-semibold">저축은행</h3>
            <button
              @click="toggleSelectAllSavingsBanks"
              class="ml-4 px-2 py-1 text-sm border rounded"
            >
              {{ isAllSavingsBanksSelected ? '전체 해제' : '전체 선택' }}
            </button>
          </div>
          <div class="grid grid-cols-4 gap-4 mt-2">
            <div
              v-for="savingsBank in savingsBanks"
              :key="savingsBank.id"
              class="flex items-center gap-2 p-2 border rounded hover:bg-gray-100 cursor-pointer"
              @click="toggleSelection(savingsBank)"
              :class="{ 'bg-blue-100': isSelected(savingsBank) }"
            >
              <img :src="savingsBank.logo || '/default-logo.png'" alt="Savings Bank Logo" class="w-8 h-8" />
              <span>{{ savingsBank.name }}</span>
            </div>
          </div>
        </section>
  
        <!-- 확인 버튼 -->
        <div class="flex justify-end mt-6">
          <button @click="confirmSelection" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
            확인
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, watch, computed } from "vue";
  
  const props = defineProps({
    banks: {
      type: Array,
      required: true,
    },
    savingsBanks: {
      type: Array,
      required: true,
    },
    selectedBanks: {
      type: Array,
      required: true,
    },
  });
  
  const emit = defineEmits(["close", "update:selectedBanks"]);
  
  const selectedBanksLocal = ref([...props.selectedBanks]);
  
  // 선택된 은행인지 확인
  const isSelected = (bank) => selectedBanksLocal.value.includes(bank.id);
  
  // 은행 선택 상태 토글
  const toggleSelection = (bank) => {
    if (isSelected(bank)) {
      selectedBanksLocal.value = selectedBanksLocal.value.filter((b) => b !== bank.id);
    } else {
      selectedBanksLocal.value.push(bank.id);
    }
  };
  
  // 은행 전체 선택 상태
  const isAllBanksSelected = computed(() => {
    return props.banks.every((bank) => selectedBanksLocal.value.includes(bank.id));
  });
  
  // 저축은행 전체 선택 상태
  const isAllSavingsBanksSelected = computed(() => {
    return props.savingsBanks.every((bank) => selectedBanksLocal.value.includes(bank.id));
  });
  
  // 은행 전체 선택/해제 토글
  const toggleSelectAllBanks = () => {
    if (isAllBanksSelected.value) {
      // 전체 해제
      selectedBanksLocal.value = selectedBanksLocal.value.filter(
        (bankId) => !props.banks.some((bank) => bank.id === bankId)
      );
    } else {
      // 전체 선택
      const bankIds = props.banks.map((bank) => bank.id);
      selectedBanksLocal.value = [...new Set([...selectedBanksLocal.value, ...bankIds])];
    }
  };
  
  // 저축은행 전체 선택/해제 토글
  const toggleSelectAllSavingsBanks = () => {
    if (isAllSavingsBanksSelected.value) {
      // 전체 해제
      selectedBanksLocal.value = selectedBanksLocal.value.filter(
        (bankId) => !props.savingsBanks.some((bank) => bank.id === bankId)
      );
    } else {
      // 전체 선택
      const bankIds = props.savingsBanks.map((bank) => bank.id);
      selectedBanksLocal.value = [...new Set([...selectedBanksLocal.value, ...bankIds])];
    }
  };
  
  // 선택 완료 시 부모 컴포넌트로 선택된 은행 목록 전달
  const confirmSelection = () => {
    emit("update:selectedBanks", selectedBanksLocal.value);
    emit("close");
  };
  
  // 부모 컴포넌트의 selectedBanks가 변경되면 로컬 상태도 업데이트
  watch(
    () => props.selectedBanks,
    (newVal) => {
      selectedBanksLocal.value = [...newVal];
    }
  );
  </script>
  
  <style scoped>
  /* 스크롤 가능 */
  .overflow-y-auto {
    overflow-y: auto;
  }
  
  /* 기본 로고 크기 */
  img {
    max-width: 40px;
    max-height: 40px;
    object-fit: cover;
  }
  
  /* 섹션 간의 여백 추가 */
  .mt-4 {
    margin-top: 1rem;
  }
  .mt-6 {
    margin-top: 1.5rem;
  }
  </style>
  