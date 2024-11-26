<template>
    <div class="bg-gray-50 min-h-screen flex justify-center items-start p-6">
        <div class="w-full max-w-5xl bg-white rounded-lg shadow-lg p-8 mt-10">
        <h1 class="text-3xl font-bold text-gray-800 text-center mb-8">고객센터</h1>
        <div class="flex justify-end mb-4">
                <!-- 글 작성하기 버튼 -->
                <button
                class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md hover:bg-blue-600 transition"                    @click="goToCreateArticle"
                >
                    글 작성하기
                </button>
            </div>
            <CSList />
        </div>
    </div>
</template>

<script setup>
import CSList from '@/components/CustomerService/CSList.vue'
import { useCsStore } from '@/stores/csStore'
import { useRouter } from 'vue-router';
import { onMounted } from 'vue'

const store = useCsStore()
const router = useRouter()
onMounted( () => {
    store.getArticles()
})

// 글 작성 페이지
const goToCreateArticle = () => {
    router.push('/cs/create'); // 새로운 글 작성 페이지로 이동
};

</script>

<style scoped>

</style>