<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white rounded-lg shadow-lg w-full max-w-md p-6">
      <!-- 모달 헤더 -->
      <div class="flex justify-between items-center pb-4 border-b border-gray-300">
        <h2 class="text-xl font-semibold text-gray-800">우대 조건 선택</h2>
        <button @click="$emit('update-preferences', selectedPreferencesLocal)" class="text-gray-600 hover:text-gray-800">
          ✕
        </button>
      </div>

      <!-- 우대 조건 목록 -->
      <div class="mt-6">
        <div v-for="(pref, index) in preferences" :key="index" class="flex items-center mb-4">
          <input
            type="checkbox"
            :value="pref"
            v-model="selectedPreferencesLocal"
            class="h-5 w-5 text-blue-600 focus:ring-blue-500 border-gray-300 rounded mr-3"
          />
          <label class="text-gray-700">{{ pref }}</label>
        </div>
      </div>

      <!-- 확인 버튼 -->
      <div class="flex justify-end mt-8">
        <button @click="$emit('update-preferences', selectedPreferencesLocal)" class="px-6 py-2 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-300">
          확인
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  preferences: {
    type: Array,
    default: () => [],
  },
  selectedPreferences: {
    type: Array,
    default: () => [],
  },
});

const emit = defineEmits(["update-preferences"]);

const selectedPreferencesLocal = ref([...props.selectedPreferences]);
</script>

<style scoped>
/* 필요 시 스타일 추가 */
</style>
