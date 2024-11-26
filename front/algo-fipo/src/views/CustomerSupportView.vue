<template>
    <div class="bg-gray-50 min-h-screen flex justify-center items-start p-6">
        <div class="w-full max-w-5xl bg-white rounded-lg shadow-lg p-8 mt-10">
        <h1 class="text-3xl font-bold text-gray-800 text-center mb-8">고객센터</h1>
        <div v-if="isLoggedIn" class="flex justify-end mb-4 mr-6">
                <!-- 글 작성하기 버튼 -->
                <button
                class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md hover:bg-blue-600 transition"                    @click="goToCreateArticle"
                >
                    글 작성하기
                </button>
            </div>
          <div v-if="articlesPerPage" class="text-center text-gray-500 py-6">작성된 문의가 없습니다.</div>
          <CSList v-else :current-page="currentPage" :articles-per-page="articlesPerPage" @changePage="changePage" />            
        </div>
    </div>
</template>

<script setup>
import CSList from '@/components/CustomerService/CSList.vue'
import { useCsStore } from '@/stores/csStore'
import { useRouter } from 'vue-router';
import { onMounted, ref } from 'vue'

const store = useCsStore()
const router = useRouter()
onMounted( () => {
    store.getArticles()
})

const isLoggedIn = !!localStorage.getItem('key')

const currentPage = ref(1);
const articlesPerPage = 10; // 페이지당 표시할 글 수

// 페이지 변경 핸들러
const changePage = (page) => {
  currentPage.value = page;
};


// 글 작성 페이지
const goToCreateArticle = () => {
    router.push('/cs/create'); // 새로운 글 작성 페이지로 이동
};

</script>

<style scoped>

</style>