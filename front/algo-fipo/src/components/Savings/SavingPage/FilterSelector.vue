
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
          <label class="text-gray-700">{{ option }}개월</label>
        </div>
      </div>
    </div>

    <!-- 상품 유형 선택 -->
    <!-- <div class="flex flex-col items-center">
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
    </div> -->

    <!-- 우대 조건 선택 -->
    <!-- <div class="flex flex-col items-center">
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
    </div> -->

    <!-- 단리/복리 선택 -->
    <div class="flex flex-col items-center">
      <label class="font-semibold text-gray-700 mb-2">단리/복리:</label>
      <div class="flex flex-col space-y-1">
        <div v-for="rateType in interestRateTypes" :key="rateType" class="flex items-center">
          <input
            type="checkbox"
            :value="rateType"
            v-model="localFilters.interestRateTypes"
            class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded mr-2"
          />
          <label class="text-gray-700">{{ rateType }}</label>
        </div>
      </div>
    </div>

    <!-- 가입 방법 선택 -->
    <div class="flex flex-col items-center">
      <label class="font-semibold text-gray-700 mb-2">가입 방법:</label>
      <div class="flex flex-col space-y-1">
        <div v-for="method in joinMethods" :key="method" class="flex items-center">
          <input
            type="checkbox"
            :value="method"
            v-model="localFilters.joinMethods"
            class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded mr-2"
          />
          <label class="text-gray-700">{{ method }}</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch, ref } from "vue";
import { debounce } from "lodash";

// Props 정의
const props = defineProps({
  filters: { type: Object, required: true },
  periodOptions: { type: Array, required: true },
  // productTypes: { type: Object, required: true },
  selectedCategory: { type: String, required: true },//이건 지우면안됨
  // preferences: { type: Array, default: () => [] },
  // selectedPreferences: { type: Array, default: () => [] },
  interestRateTypes: { type: Array, required: true },
  joinMethods: { type: Array, required: true },
});

// Emits 정의
const emit = defineEmits(["update-filters", "update-preferences"]);

// 로컬 상태 정의
const localFilters = reactive({
  durations: [...props.filters.durations],
  // types: [...props.filters.types],
  interestRateTypes: [...props.filters.interestRateTypes || []],
  joinMethods: [...props.filters.joinMethods || []],
});

// const localSelectedPreferences = ref([...props.selectedPreferences]);

// Debounce 사용
const debouncedEmitFilters = debounce((filters) => {
  emit("update-filters", filters);
}, 300);

const debouncedEmitPreferences = debounce((preferences) => {
  emit("update-preferences", preferences);
}, 300);

// Watchers
watch(
  () => props.filters,
  (newFilters) => {
    localFilters.durations = [...newFilters.durations];
    localFilters.types = [...newFilters.types];
    localFilters.interestRateTypes = [...newFilters.interestRateTypes || []];
    localFilters.joinMethods = [...newFilters.joinMethods || []];
  }
);

watch(
  () => localFilters,
  (newFilters) => {
    debouncedEmitFilters({
      durations: [...newFilters.durations],
      types: [...newFilters.types],
      interestRateTypes: [...newFilters.interestRateTypes],
      joinMethods: [...newFilters.joinMethods],
    });
  },
  { deep: true }
);

// watch(
//   () => props.selectedPreferences,
//   (newPrefs) => {
//     localSelectedPreferences.value = [...newPrefs];
//   }
// );

// watch(
//   () => localSelectedPreferences.value,
//   (newPrefs) => {
//     debouncedEmitPreferences([...newPrefs]);
//   }
// );
</script>
