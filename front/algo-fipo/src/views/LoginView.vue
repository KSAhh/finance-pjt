<template>
  <div class="flex justify-center items-center min-h-screen bg-white">
    <!-- 중앙 컨텐츠 -->
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
        <button
          class="w-full border border-gray-300 py-2 rounded text-gray-600 hover:bg-gray-100 focus:outline-none"
        >
          구글
        </button>
        <KakaoLogin />
      </div>

      <!-- 하단 링크 -->
      <div class="flex justify-between items-center mt-6 text-sm text-gray-500">
        <a href="#" class="hover:underline">비밀번호를 잊으셨나요?</a>
        <a
          @click.prevent="$router.push({ name: 'SignUpView' })"
          class="hover:underline cursor-pointer"
        >
          계정 만들기
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import KakaoLogin from "@/components/KakaoLogin/KakaoLogin.vue";

export default {
  name: "LoginView",
  components: {
    KakaoLogin,
  },
  data() {
    return {
      step: 1,
      formData: {
        username: "",
        password: "",
      },
      errorMessage: "",
    };
  },
  methods: {
    async handleFormSubmit() {
      if (this.step === 1) {
        if (this.formData.username.trim() === "") {
          this.errorMessage = "아이디를 입력해주세요.";
          return;
        }
        this.errorMessage = "";
        this.step = 2;
      } else if (this.step === 2) {
        try {
          const response = await axios.post("http://127.0.0.1:8000/accounts/login/", {
            username: this.formData.username,
            password: this.formData.password,
          });

          console.log('Response data from standard login:', response.data);

          // Adjust extraction based on actual response structure
          // Assuming similar structure to Kakao login
          const token = response.data.key && response.data.key[0] && response.data.key[0].key;
          if (!token) {
            throw new Error("Token not found in standard login response");
          }

          const fullname = response.data.fullname;

          localStorage.setItem("key", token);
          localStorage.setItem("fullname", fullname);

          // Set Axios default header
          axios.defaults.headers.common["Authorization"] = `Token ${token}`;

          // Emit event to update NavBar
          const updateNavBarEvent = new Event("updateNavBar");
          window.dispatchEvent(updateNavBarEvent);

          // Redirect to MainView
          this.$router.push({ name: "MainView" });
        } catch (error) {
          console.error("로그인 실패:", error.response?.data || error);
          this.errorMessage = "아이디 또는 비밀번호가 잘못되었습니다.";
          this.step = 1;
          this.formData.password = "";
        }
      }
    },
  },
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
