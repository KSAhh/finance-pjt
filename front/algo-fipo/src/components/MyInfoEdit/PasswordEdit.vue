<template>
    <div class="container mx-auto p-6 bg-white">
      <h1 class="text-2xl font-bold text-gray-900 mb-6">비밀번호 수정</h1>
      <p>서비스 준비중입니다. 고객센터에 문의하세요.</p>
      <button @click="goToMyInfo"
        type="submit"
        class="bg-blue-500 text-white px-4 py-2 mt-5 rounded-lg shadow-md hover:bg-blue-600 transition"
      >이전으로
      </button>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  const router = useRouter()
  const goToMyInfo = () => {
      router.push('/myinfoedit')
    };
  </script>
  
  <style scoped>
  /* Tailwind CSS 사용으로 추가 스타일링 필요하지 않음 */
  </style>
  