<!-- src/components/loan/loanpage/ProductItem.vue -->
<template>
    <div class="product-item p-4 border rounded-lg shadow hover:shadow-lg transition-shadow duration-300">
      <h2 class="text-xl font-semibold mb-2">{{ product.name }}</h2>
      <p class="text-gray-600 mb-2">금리: {{ product.rate }}%</p>
      <p class="text-gray-600 mb-2">한도: {{ product.limit.toLocaleString() }}원</p>
      <p class="text-gray-600 mb-2">대출 종류: {{ product.loanType }}</p>
      <p class="text-gray-600 mb-2">금융사: {{ product.financialCompanyId }}</p>
      <div class="features flex flex-wrap gap-2 mt-2">
        <span
          v-for="feature in product.featureIds"
          :key="feature"
          class="bg-green-200 text-green-800 px-3 py-1 rounded-full text-sm"
        >
          {{ feature }}
        </span>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    product: {
      type: Object,
      required: true,
    },
  });
  </script>
  
  <style scoped>
  .product-item {
    /* Tailwind CSS를 사용하여 스타일링 */
  }
  </style>
  