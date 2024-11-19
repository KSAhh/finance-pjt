<template>
  <div class="flex justify-center items-center min-h-screen bg-white">
    <div class="p-8 w-full max-w-md transform -translate-y-20">
      <!-- 로고 -->
      <div class="flex justify-center mb-6">
        <img src="@/assets/headerlogo.svg" alt="algo.fipo 로고" class="h-16" />
      </div>

      <!-- 안내 텍스트 -->
      <p class="text-center text-gray-600 mb-4">
        {{ step === 1 ? "아이디를 입력하세요." : "비밀번호를 입력하세요." }}
      </p>

      <!-- 동적 폼 -->
      <form @submit.prevent="handleFormSubmit">
        <div class="mb-4">
          <input
            v-if="step === 1"
            v-model="formData.username"
            type="text"
            placeholder="아이디를 입력하세요."
            class="w-full border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
            required
          />
          <input
            v-else
            v-model="formData.password"
            type="password"
            placeholder="비밀번호를 입력하세요."
            class="w-full border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
            required
          />
        </div>
        <div>
          <button
            type="submit"
            class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 focus:outline-none focus:ring"
          >
            {{ step === 1 ? "다음" : "로그인" }}
          </button>
        </div>
      </form>

      <!-- 에러 메시지 -->
      <p v-if="errorMessage" class="text-red-500 text-center mt-4">
        {{ errorMessage }}
      </p>

      <!-- 또는 다른 방법으로 로그인 -->
      <p class="text-center text-gray-500 mt-6 mb-2">또는 다음을 사용하여 계속하기</p>
      <div class="space-y-2">
        <!-- 구글 로그인 버튼 (추후 구현 필요) -->
        <button
          class="w-full border border-gray-300 py-2 rounded text-gray-600 hover:bg-gray-100 focus:outline-none"
        >
          구글
        </button>
        <!-- 카카오톡 로그인 -->
        <KakaoLogin />
      </div>

      <!-- 하단 링크 -->
      <div class="flex justify-between items-center mt-6 text-sm text-gray-500">
        <a href="#" class="hover:underline">비밀번호를 잊으셨나요?</a>
        <a
          @click.prevent="goToSignUp"
          class="hover:underline cursor-pointer"
        >
          계정 만들기
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { useNavBarStore } from "@/stores/navBarStore";
import KakaoLogin from "@/components/KakaoLogin/KakaoLogin.vue"; // 카카오톡 로그인 컴포넌트

const router = useRouter();
const navBarStore = useNavBarStore();

const step = ref(1);
const formData = reactive({
  username: "",
  password: "",
});
const errorMessage = ref("");

// 회원가입 페이지로 이동
const goToSignUp = () => {
  router.push({ name: "SignUpView" });
};

// 일반 로그인 처리
const handleFormSubmit = async () => {
  if (step.value === 1) {
    if (!formData.username.trim()) {
      errorMessage.value = "아이디를 입력해주세요.";
      return;
    }
    errorMessage.value = "";
    step.value = 2;
  } else if (step.value === 2) {
    try {
      const response = await axios.post("http://127.0.0.1:8000/accounts/login/", {
        username: formData.username,
        password: formData.password,
      });

      const token = response.data.key;
      const fullname = response.data.fullname || "사용자 이름 없음";

      if (!token) {
        throw new Error("Token not found in response");
      }

      // LocalStorage 저장
      localStorage.setItem("key", token);
      localStorage.setItem("fullname", fullname);

      // Axios 기본 헤더 설정
      axios.defaults.headers.common["Authorization"] = `Token ${token}`;

      // NavBar 상태 업데이트
      navBarStore.login(fullname);

      // 메인 페이지로 이동
      router.push({ name: "MainView" });
    } catch (error) {
      console.error("로그인 실패:", error.response?.data || error);
      errorMessage.value = "아이디 또는 비밀번호가 잘못되었습니다.";
      step.value = 1;
      formData.password = "";
    }
  }
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
