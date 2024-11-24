<template>
  <div>
    <h3>Article List</h3>
    <CSListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"/>
  </div>

</template>

<script setup>
import { useCsStore } from '@/stores/csStore'
import CSListItem from './CSListItem.vue';
const store = useCsStore()

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