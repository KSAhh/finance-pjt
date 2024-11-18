<template>
  <div class="flex justify-center items-center min-h-screen bg-white">
    <!-- 중앙 컨텐츠 -->
    <div class="p-8 w-full max-w-md">
      <!-- 로고 -->
      <div class="flex justify-center mb-6">
        <img src="@/assets/headerlogo.svg" alt="algo.fipo 로고" class="h-16" />
      </div>

      <!-- 안내 텍스트 -->
      <p class="text-center text-gray-600 mb-4">계속하려면 로그인하세요.</p>

      <!-- 이메일 입력 폼 -->
      <form>
        <div class="mb-4">
          <input
            type="email"
            placeholder="이메일을 입력하세요."
            class="w-full border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
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

      <!-- 또는 다른 방법으로 로그인 -->
      <p class="text-center text-gray-500 mt-6 mb-2">또는 다음을 사용하여 계속하기</p>

      <!-- 소셜 로그인 버튼 -->
      <div class="space-y-2">
        <button
          class="w-full border border-gray-300 py-2 rounded text-gray-600 hover:bg-gray-100 focus:outline-none"
        >
          구글
        </button>
        <button
          class="w-full border border-gray-300 py-2 rounded text-gray-600 hover:bg-gray-100 focus:outline-none"
        >
          카카오톡
        </button>
      </div>

      <!-- 하단 링크 -->
      <div class="flex justify-between items-center mt-6 text-sm text-gray-500">
        <a href="#" class="hover:underline">비밀번호를 잊으셨나요?</a>
        <a href="#" class="hover:underline">계정 만들기</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
};
</script>

<style scoped>
/* 화면 조정 스타일 */
html,
body,
#app {
  height: 100%;
  margin: 0;
}

.min-h-screen {
  height: calc(100vh - 64px); /* NavBar 높이를 제외한 나머지 영역 */
}
</style>
