<template>
    <div>
      <h2 class="text-2xl font-semibold mb-4">{{ title }}</h2>
      <div v-if="products && products.length > 0">
            <ul class="divide-y divide-gray-300">
                <MyProductListItem
                    v-for="product in products"
                    :key="product.id"
                    :product="product"
                    />
            </ul>
        </div>
        <div v-else class="text-gray-500 text-sm">
            가입하고싶은 상품을 찾아보세요!
        </div>
    </div>
  </template>
  
  <script setup>
  import MyProductListItem from '@/components/mypage/MyProductListItem.vue'
  
  defineProps({
    products: Array,
    title: String,
  })

  </script>
  
  <style scoped>
  /* Tailwind CSS 사용 */
  </style>
  