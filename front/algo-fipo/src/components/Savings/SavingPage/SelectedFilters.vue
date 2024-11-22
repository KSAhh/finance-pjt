<template>
  <div v-if="filters.length > 0" class="mt-6">
    <span class="text-sm text-gray-600">선택된 필터:</span>
    <div class="flex flex-wrap gap-3 mt-3">
      <div
        v-for="(filter, index) in filters"
        :key="index"
        class="flex items-center bg-blue-100 text-blue-600 px-3 py-1 rounded-full text-sm cursor-pointer"
        @click="$emit('remove-filter', filter)"
      >
        <span>{{ filter }}</span>
        <button class="ml-2 text-blue-500 hover:text-blue-700 focus:outline-none">
          &times;
        </button>
      </div>
    </div>
  </div>
</template>
  
  <script setup>
  defineProps({
    filters: Array,
  });
  </script>
  
  <style scoped>
  /* 스타일 필요 시 작성 */
  </style>
  