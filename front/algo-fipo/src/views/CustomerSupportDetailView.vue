<template>
    <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>글 번호 : {{ article.id }}</p>
      <p>제목 : {{ article.title }}</p>
      <!-- <p>내용 : {{ article.content }}</p> -->
      <p>작성시간 : {{ article.created_at }}</p>
      <p>수정시간 : {{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCsStore } from '@/stores/csStore'

const store = useCsStore()
const route = useRoute()
const article = ref(null)
const API_URL = "http://127.0.0.1:8000"

console.log(route.params.article_pk); // article_pk 값 확인

onMounted(async () => {
    await axios.get(`${store.API_URL}/api/v1/articles/${route.params.article_pk}/`)
    await axios.get(`http://127.0.0.1:8000/api/v1/articles/${route.params.article_pk}/`)
    .then((res) => {
        console.log(res.data)
        article.value = res.data.article
    })
    .catch(err => console.log("오류", err))
})
</script>

<style scoped>
</style>