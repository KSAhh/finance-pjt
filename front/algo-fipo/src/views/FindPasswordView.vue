<template>
    <div class="flex justify-center items-center min-h-screen bg-white">
      <div class="p-8 w-full max-w-md transform -translate-y-20">
        <!-- 로고 -->
        <div class="flex justify-center mb-6">
          <img src="@/assets/headerlogo.svg" alt="algo.fipo 로고" class="h-16" />
        </div>
  
        <!-- 안내 텍스트 -->
        <p class="text-center text-gray-600 mb-4">
          비밀번호를 찾고자 하는 이메일을 입력해주세요.
        </p>
  
        <!-- 이메일 입력 폼 -->
        <form @submit.prevent="findPassword">
          <div class="mb-4">
            <input
              v-model="email"
              type="email"
              placeholder="이메일을 입력하세요."
              class="w-full border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
              required
            />
          </div>
          <div>
            <button
              type="submit"
              class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 focus:outline-none focus:ring"
            >
              계속
            </button>
          </div>
        </form>
  
        <!-- 추가 인증 옵션 -->
        <p class="text-center text-gray-500 mt-6 mb-2">이메일을 잊으셨나요?</p>
        <div class="space-y-2">
          <button
            class="w-full border border-gray-300 py-2 rounded text-gray-600 hover:bg-gray-100 focus:outline-none"
          >
            휴대전화 인증
          </button>
          <button
            class="w-full border border-gray-300 py-2 rounded text-gray-600 hover:bg-gray-100 focus:outline-none"
          >
            카카오톡 인증
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const email = ref("");
  
  const findPassword = () => {
    if (!email.value.trim()) {
      alert("이메일을 입력해주세요.");
      return;
    }
  
    // 비밀번호 찾기 요청 로직 추가
    alert(`비밀번호 찾기 요청: ${email.value}`);
  };
  </script>
  
  <style scoped>
  .min-h-screen {
    height: calc(100vh - 64px); /* NavBar 높이를 제외한 나머지 영역 */
  }
  </style>
  