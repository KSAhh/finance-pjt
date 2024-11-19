<template>
  <button
    @click="goToLogin"
    class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 whitespace-nowrap"
  >
    로그인
  </button>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

// LoginView로 이동하는 함수
const goToLogin = () => {
  router.push({ name: "LoginView" });
};
</script>

<style scoped>
/* 필요 시 추가 스타일 작성 */
</style>
