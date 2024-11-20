<template>
  <div>
    <p v-if="products.length === 0" class="text-center text-gray-500 mt-10">
      표시할 상품이 없습니다.
    </p>
    <ul v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mt-8">
      <li
        v-for="product in products"
        :key="product.id"
        class="border border-gray-200 rounded-lg shadow p-6 hover:shadow-lg transition-shadow duration-300"
      >
        <h3 class="text-xl font-semibold mb-3 text-gray-800">{{ product.name }}</h3>
        <p class="text-gray-600 mb-4">{{ product.description }}</p>
        <div class="flex items-center justify-between">
          <p class="text-blue-600 font-bold text-lg">{{ product.rate }}%</p>
          <button class="px-4 py-2 bg-yellow-400 text-gray-800 rounded-lg hover:bg-yellow-500 transition duration-300">
            상세보기
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  products: {
    type: Array,
    required: true,
  },
});
</script>

<style scoped>
/* 추가적인 스타일이 필요한 경우 여기에 작성하세요 */
</style>
