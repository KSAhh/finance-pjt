<template>
  <div class="bg-gray-50 min-h-screen p-6">
    <div class="w-full max-w-4xl mx-auto space-y-8">
      <CSListItemDetailArticle />
      <!-- 댓글 -->
      <CSListItemDetailComment
        :articlePk="articlePk"
        :articleAuthorId="article.author"
        />
    </div>
    <div class="flex justify-center mb-4 mt-4">
      <button 
        @click="goToList"
        class="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600 transition"
      >
        목록으로 가기
      </button>
    </div>
  </div>

</template>

<script setup>
// {
//         "image": null,
//         "is_private": false,
//         "is_delete": false,
//         "created_at": "2024-11-18T07:04:29.255492Z",
//         "updated_at": "2024-11-18T07:04:29.255492Z",
//         "author": 11
//     },

import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCsStore } from '@/stores/csStore'
import CSListItemDetailArticle from '@/components/CustomerService/CSListItemDetailArticle.vue'
import CSListItemDetailComment from '@/components/CustomerService/CSListItemDetailComment.vue'

const store = useCsStore()
const route = useRoute()
const router = useRouter()
const articlePk = route.params.article_pk;

const comments = computed(() => store.comments[articlePk] || []); // 특정 글의 댓글 데이터 가져오기
const article = computed(() => store.article || {} )
const API_URL = import.meta.env.VITE_API_BASE_URL

onMounted(async () => {
  await store.getArticle(articlePk)
})

// 글 수정 함수
const updateArticle = () => {
  const newTitle = prompt('새 제목을 입력하세요:', article.value.title);
  const newContent = prompt('새 내용을 입력하세요:', article.value.article_body);

  if (newTitle && newContent) {
    store.updateArticle(articlePk, { title: newTitle, article_body: newContent });
  }
}

// 글 삭제 함수
const deleteArticle = () => {
  if (confirm('정말로 글을 삭제하시겠습니까?')) {
    store.deleteArticle(articlePk);
  }
}

// 댓글 수정 함수
const updateComment = () => {
  const newContent = prompt('댓글 내용을 수정하세요:');

  if (newContent) {
    store.updateComment(commentId, { comment_body: newContent });
  }
}

// 댓글 삭제 함수
const deleteComment = (commentId) => {
  if (confirm('정말로 댓글을 삭제하시겠습니까?')) {
    store.deleteComment(commentId);
  }
}

// 목록 이동 함수
const goToList = () => {
  router.push('/cs')
}
</script>

<style scoped>
button {
  margin: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
}

button {
  font-size: 0.875rem;

  margin: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #fff; /* 기본 배경 흰색 */
  color: #000; /* 기본 텍스트 검은색 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 기본 쉐도우 */
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; /* 부드러운 전환 효과 */
}

button:hover {
  background-color: #000; /* 호버 시 배경 검은색 */
  color: #fff; /* 호버 시 텍스트 흰색 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 호버 시 쉐도우 더 강조 */
}
/* 추가된 컴포넌트 간 간격 제거 */
.space-y-8 > * + * {
  margin-top: 2rem;
}
</style>