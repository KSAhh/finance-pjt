<template>
  <div v-if="filters.length > 0" class="mt-4 border rounded p-4 bg-gray-50">
    <span class="text-sm text-gray-500">선택된 필터:</span>
    <div class="flex flex-wrap gap-2 mt-2">
      <div
        v-for="(filter, index) in filters"
        :key="index"
        class="px-3 py-1 bg-blue-100 text-blue-600 rounded-full text-sm cursor-pointer"
        @click="$emit('remove-filter', filter)"
      >
        {{ filter }}
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  filters: Array,
});

defineEmits(["remove-filter"]);
</script>

<style scoped>
/* 필요 시 스타일 추가 */
</style>
