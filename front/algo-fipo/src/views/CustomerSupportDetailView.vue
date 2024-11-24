<template>
    <div v-if="article">
        <p>게시글 번호 : {{ article.id }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.article_body }}</p>
    </div>
    <p v-else>로딩 중...</p>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCsStore } from '@/stores/csStore'

const store = useCsStore()
const route = useRoute()
const article = ref(null)

console.log(route.params.article_pk); // article_pk 값 확인

onMounted(async () => {
    // axios.get(`${store.API_URL}/api/v1/articles/${route.params.article_pk}/`)
    await axios.get(`${store.API_URL}/api/v1/articles/3/`)
    .then((res) => {
        console.log(res.data)
        article.value = res.data.article
    })
    .catch(err => console.log("오류", err))
})
</script>

<style scoped>
</style>