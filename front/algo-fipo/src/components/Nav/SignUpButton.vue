<template>
  <button
    @click="goToSignUp"
    class="bg-gray-200 text-black px-4 py-2 rounded hover:bg-gray-300 whitespace-nowrap"
  >
    회원가입
  </button>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goToSignUp = () => {
  router.push({ name: "SignUpView" }); // SignUpView로 이동
};
</script>
