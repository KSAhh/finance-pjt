<template>
  <div class="flex flex-wrap items-start justify-center gap-8">
    <!-- 기간 선택 -->
    <div class="flex flex-col items-center">
      <label class="font-semibold text-gray-700 mb-2">기간:</label>
      <div class="flex flex-col space-y-1">
        <div v-for="option in periodOptions" :key="option" class="flex items-center">
          <input
            type="checkbox"
            :value="option"
            v-model="localFilters.durations"
            class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded mr-2"
          />
          <label class="text-gray-700">{{ option }}</label>
        </div>
      </div>
    </div>

    <!-- 상품 유형 선택 -->
    <div class="flex flex-col items-center">
      <label class="font-semibold text-gray-700 mb-2">상품 유형:</label>
      <div class="flex flex-col space-y-1">
        <div
          v-for="type in productTypes[selectedCategory]"
          :key="type"
          class="flex items-center"
        >
          <input
            type="checkbox"
            :value="type"
            v-model="localFilters.types"
            class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded mr-2"
          />
          <label class="text-gray-700">{{ type }}</label>
        </div>
      </div>
    </div>

    <!-- 우대 조건 선택 -->
    <div class="flex flex-col items-center">
      <label class="font-semibold text-gray-700 mb-2">우대 조건:</label>
      <div class="flex flex-col space-y-1">
        <div v-for="pref in preferences" :key="pref" class="flex items-center">
          <input
            type="checkbox"
            :value="pref"
            v-model="localSelectedPreferences"
            class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded mr-2"
          />
          <label class="text-gray-700">{{ pref }}</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch, ref } from "vue";

const props = defineProps({
  filters: {
    type: Object,
    required: true,
  },
  periodOptions: {
    type: Array,
    required: true,
  },
  productTypes: {
    type: Object,
    required: true,
  },
  selectedCategory: {
    type: String,
    required: true,
  },
  preferences: {
    type: Array,
    default: () => [],
  },
  selectedPreferences: {
    type: Array,
    default: () => [],
  },
});

const emit = defineEmits(["update-filters", "update-preferences"]);

const localFilters = reactive({
  durations: [...props.filters.durations],
  types: [...props.filters.types],
});

const localSelectedPreferences = ref([...props.selectedPreferences]);

watch(
  () => props.filters,
  (newFilters) => {
    localFilters.durations = [...newFilters.durations];
    localFilters.types = [...newFilters.types];
  }
);

watch(
  () => localFilters,
  (newFilters) => {
    emit("update-filters", { durations: [...newFilters.durations], types: [...newFilters.types] });
  },
  { deep: true }
);

watch(
  () => props.selectedPreferences,
  (newPrefs) => {
    localSelectedPreferences.value = [...newPrefs];
  }
);

watch(
  () => localSelectedPreferences.value,
  (newPrefs) => {
    emit("update-preferences", [...newPrefs]);
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
