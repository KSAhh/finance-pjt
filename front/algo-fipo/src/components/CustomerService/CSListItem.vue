<template>
  <div class="border rounded-lg shadow-md p-4 bg-white flex items-start">
    <img 
      v-if="article.image" 
      :src="article.image" 
      alt="article image" 
      class="w-12 h-12 rounded-full object-cover mr-4"
    />
    <div class="flex-1">
      <div class="flex justify-between items-center mb-2">
        <h5 class="text-lg font-semibold text-gray-800">{{ article.title }}</h5>
        <span class="text-sm text-gray-500">{{ formatDate(article.created_at) }}</span>
      </div>
      <p class="text-sm text-gray-600 mb-2 trim-box">{{ article.article_body }}</p>
      <div class="flex items-center justify-between text-sm text-gray-500">
        <span>작성자: <span class="font-medium text-gray-800">{{ article.author_nickname }}</span></span>
        <RouterLink 
          :to="{ name: 'CustomerSupportDetail', params: { article_pk: article.id }}"
          class="text-blue-500 hover:underline"
        >
          상세보기
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { truncate } from 'lodash'
import { watch, ref } from 'vue'

defineProps({
  article: Object,
})

// 날짜 포맷 함수
const formatDate = (date) => {
  return new Date(date).toLocaleDateString("ko-KR", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  })
}

// {
//         "image": null,
//         "is_private": false,
//         "is_delete": false,
//         "created_at": "2024-11-18T07:04:29.255492Z",
//         "updated_at": "2024-11-18T07:04:29.255492Z",
//         "author": 11
//     },


</script>

<style scoped>
/* 본문 글자수 제한이 추가로 필요할 경우 */
p.text-sm {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>