<!-- <template>
    <div class="mt-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-if="products.length > 0"
        v-for="item in products"
        :key="item.id"
        class="border rounded-lg p-4 shadow hover:shadow-lg"
      >
        <h3 class="text-lg font-semibold">{{ item.name }}</h3>
        <p class="text-sm text-gray-500">{{ item.description }}</p>
        <p class="mt-2 text-blue-600 font-bold">금리: {{ item.rate }}%</p>
      </div>
      <div v-else class="border rounded-lg p-4 text-center text-gray-500 col-span-full">
        표시할 상품이 없습니다.
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    products: Array,
  });
  </script>
  
  <style scoped>
  /* 스타일 필요 시 작성 */
  </style>
   -->