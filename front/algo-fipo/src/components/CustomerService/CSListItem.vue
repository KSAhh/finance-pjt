<template>
  <div
    v-if="!article.is_private || article.author === currentUserId"
    class="border rounded-lg shadow-md p-4 bg-white flex items-start"
  >

    <div class="flex-1">
      <div class="flex justify-between items-center mb-2">
        <h5 class="text-lg font-semibold text-gray-800">{{ article.title }}</h5>
        <span class="text-sm text-gray-500">{{ formatDate(article.created_at) }}</span>
      </div>
      <p v-if="article.is_private && article.author === currentUserId" class="text-sm text-red-500">
        내가 작성한 비밀 글
      </p>
      <p class="text-sm text-gray-600 mb-2 trim-box">{{ truncatedArticleBody }}</p>
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
import { watch, ref, computed, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const props = defineProps({
  article: Object,
})

onMounted( async () => {
  await userStore.getUserInfo() // 사용자 정보 가져오기
})

// 날짜 포맷 함수
const formatDate = (date) => {
  return new Date(date).toLocaleDateString("ko-KR", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  })
}

const userStore = useUserStore()
const currentUserId = computed(() => userStore.userInfo.pk) // 현재 사용자 ID

const truncatedArticleBody = ref("");
watch(
  () => props.article, // 관찰할 값
  (newArticle) => {
    if (newArticle && newArticle.article_body) {
      // 본문을 truncate로 자르기
      truncatedArticleBody.value = truncate(newArticle.article_body, {
        length: 30, // 최대 길이
        omission: "...", // 생략 표시
      });
    } else {
      truncatedArticleBody.value = ""; // 본문이 없으면 빈 문자열
    }
  },
  { immediate: true } // 초기값 관찰
);

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

</style>