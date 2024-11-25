<template>
    <div class="bg-gray-50 min-h-screen flex justify-center items-start p-6">
        <div class="w-full max-w-5xl bg-white rounded-lg shadow-lg p-8 mt-10">
        <h1 class="text-3xl font-bold text-gray-800 text-center mb-8">고객센터</h1>
        <CSList />
        </div>
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