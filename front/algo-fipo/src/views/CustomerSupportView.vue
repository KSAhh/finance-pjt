<template>
    <h1>고객센터</h1>
    <div v-if="store.articles.length === 0">작성된 글이 없습니다.</div>
    <div v-else>
        <CSList 
            v-for="article in store.articles"
            :key="article.id"
            :article="article"
        />
    </div>
</template>

<script setup>
import CSList from '@/components/CustomerService/CSList.vue'
import { useCsStore } from '@/stores/csStore'
import { onMounted } from 'vue';

const store = useCsStore()
onMounted( () => {
    store.getArticles()
})

</script>

<style scoped>
</style>