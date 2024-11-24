<template>
   <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <!-- <p>{{ article.content }}</p> -->
    <RouterLink :to="{ name: 'CustomerSupportDetail', params: { article_pk: article.id }}">[DETAIL]</RouterLink>
    <RouterView/>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

defineProps({
  article: Object,
})
</script>

<style scoped>

</style>