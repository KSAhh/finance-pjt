<template>
  <div>
    <div v-if="article">
    <h5>글번호: {{ article.id }}</h5>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.article_body }}</p>
    <div v-if="article.image">
      <img :src="article.image" alt="첨부이미지">
    </div>
    <p>작성일 : {{ article.created_at }}</p>
    <p>작성자 : {{ article.author }}</p>
    <RouterLink :to="{ name: 'CustomerSupportDetail', params: { article_pk: article.id } }">[DETAIL]</RouterLink>
    </div>
    <p v-else>유효한 글이 없습니다.</p>

    <!-- <h5>글번호: {{ article.id }}</h5> -->
    <!-- <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.article_body }}</p>
    <div v-if="article.image">
      <img :src="article.image" alt="첨부이미지">
    </div>    <p>작성일 : {{ article.created_at }}</p>
    <p>작성자 : {{ article.author }}</p>
    <RouterLink v-if="article.id" :to="{ name: 'CustomerSupportDetail', params: {article_pk: article.id}}">[DETAIL]</RouterLink> -->
  </div>
</template>

<script setup>
import { useCsStore } from '@/stores/csStore'
import { RouterLink } from 'vue-router'
const store = useCsStore()

defineProps({
  article: Object,
})
// {
//         "id": 1,
//         "title": "글 제목",
//         "article_body": "글 본문",
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