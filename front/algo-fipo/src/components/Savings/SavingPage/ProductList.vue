<template>
  <div>
    <p v-if="products.length === 0" class="text-center text-gray-500">
      표시할 상품이 없습니다.
    </p>
    <ul v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      <li
        v-for="product in products"
        :key="product.id"
        class="border rounded-lg shadow p-4"
      >
        <h3 class="text-lg font-semibold mb-2">{{ product.name }}</h3>
        <p class="text-gray-600">{{ product.description }}</p>
        <p class="text-gray-800 font-bold mt-2">{{ product.rate }}%</p>
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
.grid {
  display: grid;
}
.gap-4 {
  gap: 1rem;
}
</style>
