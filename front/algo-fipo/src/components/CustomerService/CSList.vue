<template>
    <div class="max-w-screen-xl p-6 min-h-screen">
      <div class="space-y-4">
        <CSListItem 
          v-for="article in store.articles"
          :key="article.id"
          :article="article"
        />
      </div>
    </div>
</template>

<script setup>
import { useCsStore } from '@/stores/csStore'
import CSListItem from './CSListItem.vue';
const store = useCsStore()

</script>

<style scoped>
</style>