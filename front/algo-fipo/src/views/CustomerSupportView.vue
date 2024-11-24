<template>
    <h1>고객센터</h1>
    <CSList />
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