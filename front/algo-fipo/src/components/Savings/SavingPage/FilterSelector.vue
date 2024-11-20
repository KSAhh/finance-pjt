<template>
  <div class="mt-6 space-y-4">
    <div class="flex justify-between items-center">
      <!-- 기간 -->
      <div>
        <span class="text-sm text-gray-500">기간:</span>
        <select
          v-model="localFilters.duration"
          class="border p-2 rounded"
          @change="emitFilters"
        >
          <option value="">전체</option>
          <option value="6개월">6개월</option>
          <option value="12개월">12개월</option>
          <option value="24개월 이상">24개월 이상</option>
        </select>
      </div>
      <!-- 상품 유형 -->
      <div>
        <span class="text-sm text-gray-500">상품 유형:</span>
        <select
          v-model="localFilters.type"
          class="border p-2 rounded"
          @change="emitFilters"
        >
          <option value="">전체</option>
          <!-- 상품 유형을 동적으로 렌더링 -->
          <option
            v-for="type in productTypes[selectedCategory]"
            :key="type"
            :value="type"
          >
            {{ type }}
          </option>
        </select>
      </div>
      <!-- 우대 조건 -->
      <div>
        <span class="text-sm text-gray-500">우대 조건:</span>
        <button
          @click="$emit('toggle-preferences')"
          class="border p-2 rounded bg-gray-100 hover:bg-gray-200"
        >
          {{ selectedPreferences.length > 0 ? `우대 조건 ${selectedPreferences.length}개` : "전체" }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch } from "vue";

const props = defineProps({
  filters: Object, // 필터 데이터
  productTypes: Object, // 상품 유형 (예금/적금에 따라 다름)
  selectedCategory: String, // 현재 선택된 카테고리 (예: 예금, 적금)
  selectedPreferences: Array, // 현재 선택된 우대 조건
});

const emit = defineEmits(["update-filters", "toggle-preferences"]);

const localFilters = reactive({ ...props.filters });

// 필터 변경 시 부모 컴포넌트로 emit
const emitFilters = () => {
  emit("update-filters", { ...localFilters });
};

watch(
  () => props.filters,
  (newVal) => {
    Object.assign(localFilters, newVal);
  }
);
</script>

<style scoped>
.border {
  border-color: #d1d5db; /* 기본 테두리 색상 */
}
.rounded {
  border-radius: 0.375rem; /* 기본 테두리 반경 */
}
</style>
