<template>
    <div class="max-w-screen-xl p-6 min-h-screen">
      <div class="space-y-4">
        
        <CSListItem 
          v-for="article in paginatedArticles"
          :key="article.id"
          :article="article"
        />
        <!-- 페이지네이션 -->
        <div class="flex justify-center mt-6">
          <button
            v-for="page in totalPages"
            :key="page"
            @click="emitChangePage(page)"
            class="px-3 py-1 mx-1 border rounded-lg"
            :class="{
              'bg-blue-500 text-white': props.currentPage === page,
              'bg-gray-100 hover:bg-gray-200': props.currentPage !== page,
            }"
          >
            {{ page }}
          </button>
        </div>

      </div>
    </div>
</template>

<script setup>
import { useCsStore } from '@/stores/csStore'
import { computed, defineEmits } from 'vue'
import CSListItem from './CSListItem.vue'

const store = useCsStore()

const props = defineProps({
  currentPage: Number,
  articlesPerPage: Number,
});
const emit = defineEmits(["changePage"]);


const paginatedArticles = computed(() => {
  const startIndex = (props.currentPage - 1) * props.articlesPerPage;
  const endIndex = startIndex + props.articlesPerPage;
  return store.articles.slice(startIndex, endIndex); // 현재 페이지의 글만 가져옴
});

const totalPages = computed(() => {
  return Math.ceil(store.articles.length / props.articlesPerPage);
});

const emitChangePage = (page) => {
  emit('changePage', page);
};

</script>

<style scoped>
</style>