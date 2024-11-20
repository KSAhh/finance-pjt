<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white rounded-lg shadow-lg w-1/2 p-6">
      <!-- 모달 헤더 -->
      <div class="flex justify-between items-center pb-4 border-b border-gray-300">
        <h2 class="text-lg font-semibold">우대 조건 선택</h2>
        <button @click="$emit('update-preferences', selectedPreferencesLocal)" class="text-gray-600 hover:text-black">✕</button>
      </div>

      <!-- 우대 조건 목록 -->
      <div class="mt-4">
        <div v-for="(pref, index) in preferences" :key="index" class="flex items-center mb-2">
          <input
            type="checkbox"
            :value="pref"
            v-model="selectedPreferencesLocal"
            class="mr-2"
          />
          <label>{{ pref }}</label>
        </div>
      </div>

      <!-- 확인 버튼 -->
      <div class="flex justify-end mt-6">
        <button @click="$emit('update-preferences', selectedPreferencesLocal)" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
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
