<template>
    <div class="flex justify-center space-x-4">
      <button
        v-for="category in categories"
        :key="category"
        :class="[
          'px-4 py-2 rounded-lg',
          selectedCategory === category
            ? 'bg-blue-500 text-white'
            : 'bg-gray-200 text-gray-700',
        ]"
        @click="$emit('select-category', category)"
      >
        {{ category }}
      </button>
    </div>
  </template>
  
  <script setup>
  defineProps({
    categories: {
      type: Array,
      required: true,
    },
    selectedCategory: {
      type: String,
      required: true,
    },
  });
  
  defineEmits(["select-category"]);
  </script>
  
  <style scoped>
  .flex {
    display: flex;
  }
  .space-x-4 > * + * {
    margin-left: 1rem;
  }
  </style>
  