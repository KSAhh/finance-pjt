<template>
    <!-- <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>글 번호 : {{ article.id }}</p>
      <p>{{ article.author_nickname }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.article_body }}</p>
      <p>작성시간 : {{ article.created_at }}</p>
      <p>수정시간 : {{ article.updated_at }}</p>
    </div>
  </div> -->
  <div>
    <h1>글 상세</h1>
    <div v-if="article">
      <p>글 번호: {{ article.id }}</p>
      <p>작성자: {{ article.author_nickname }}</p>
      <p>제목: {{ article.title }}</p>
      <p>내용: {{ article.article_body }}</p>
    </div>
    <div v-else>
      <p>글을 불러오는 중...</p>
    </div>

    <h2 class="mt-6">댓글 목록</h2>
    <div v-if="comments && comments.length > 0">
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>댓글작성자: {{ comment.commenter_nickname }}</p>
          <p>내용: {{ comment.comment_body }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>댓글이 없습니다.</p>
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
import { useRoute } from 'vue-router'
import { useCsStore } from '@/stores/csStore'

const store = useCsStore()
const route = useRoute()
const articlePk = route.params.article_pk;

const comments = computed(() => store.comments[articlePk] || []); // 특정 글의 댓글 데이터 가져오기
const article = computed(() =>
  store.articles.find((item) => item.id == articlePk)
); // 이미 불러온 글 데이터 사용
const API_URL = import.meta.env.VITE_API_BASE_URL

onMounted(async () => {
  await store.getComments(articlePk)
})
</script>

<style scoped>
</style>