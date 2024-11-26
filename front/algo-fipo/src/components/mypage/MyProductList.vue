<template>
  <div class="bg-gray-50 p-6 rounded-lg shadow-md">
    <h2 class="text-2xl font-semibold text-gray-800 mb-6 border-b pb-2">{{ title }}</h2>
    <div v-if="products && products.length > 0">
      <ul class="space-y-4">
        <MyProductListItem
          v-for="product in products"
          :key="product.id"
          :product="product"
          class="bg-white rounded-lg shadow-lg p-4 hover:shadow-xl transition"
        />
      </ul>
    </div>
    <div v-else class="text-gray-500 text-center mt-4 text-sm">
      가입하고 싶은 상품을 찾아보세요!
    </div>
  </div>
</template>

<script setup>
import MyProductListItem from "@/components/mypage/MyProductListItem.vue";

defineProps({
  products: Array,
  title: String,
});
</script>

<style scoped>
/* Tailwind CSS 사용 - 필요하면 아래 설정 추가 */
</style>
