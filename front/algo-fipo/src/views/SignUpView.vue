<template>
    <div class="flex justify-center items-center min-h-screen bg-white">
      <div class="p-8 w-full max-w-md transform -translate-y-20">
        <!-- 로고 -->
        <div class="flex justify-center mb-6">
          <img src="@/assets/headerlogo.svg" alt="algo.fipo 로고" class="h-16" />
        </div>
  
        <!-- 안내 텍스트 -->
        <p class="text-center text-gray-600 mb-4">계정을 만들어 서비스를 이용하세요.</p>
  
        <!-- 회원가입 폼 -->
        <form @submit.prevent="signup">
          <div class="mb-4">
            <input
              v-model="formData.username"
              type="text"
              placeholder="사용자 이름"
              class="w-full border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
              required
            />
          </div>
          <div class="mb-4">
            <input
              v-model="formData.password"
              type="password"
              placeholder="비밀번호"
              class="w-full border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
              autocomplete="off"
              @keydown="preventUndo"
              required
            />
          </div>
          <div class="mb-4">
            <input
              v-model="formData.confirmPassword"
              :class="{
                'border-red-500': formData.password !== formData.confirmPassword && formData.confirmPassword !== '',
                'border-gray-300': formData.password === formData.confirmPassword || formData.confirmPassword === '',
              }"
              type="password"
              placeholder="비밀번호 확인"
              class="w-full border rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
              autocomplete="off"
              @keydown="preventUndo"
              required
            />
            <p
              v-if="formData.password !== formData.confirmPassword && formData.confirmPassword !== ''"
              class="text-red-500 text-sm mt-1"
            >
              비밀번호가 일치하지 않습니다.
            </p>
          </div>
          <div class="mb-4">
              <input
              v-model="formData.nickname"
              type="text"
              placeholder="별명"
              class="w-full border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
              required
              />
            </div>
            <div class="mb-4">
              <input
                v-model="formData.fullname"
                type="text"
                placeholder="실명"
                class="w-full border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500"
                required
              />
            </div>
          <div>
            <button
              type="submit"
              class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 focus:outline-none focus:ring"
              :disabled="formData.password !== formData.confirmPassword || formData.password === ''"
            >
              회원가입
            </button>
          </div>
        </form>
  
        <!-- 하단 링크 -->
        <div class="flex justify-between items-center mt-6 text-sm text-gray-500">
          <a @click.prevent="goToLogin" class="hover:underline cursor-pointer">이미 계정이 있으신가요?</a>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "SignUpView",
    data() {
      return {
        formData: {
          username: "",
          password: "",
          confirmPassword: "",
          nickname: "",
          fullname: "",
        },
      };
    },
    methods: {
      preventUndo(event) {
        // Ctrl + Z 감지
        if ((event.ctrlKey || event.metaKey) && event.key === "z") {
          event.preventDefault();
        }
      },
      async signup() {
        if (this.formData.password !== this.formData.confirmPassword) {
          alert("비밀번호가 일치하지 않습니다.");
          return;
        }
  
        try {
          // JSON 데이터로 요청 보내기
          const data = await axios.post("http://127.0.0.1:8000/accounts/signup/", {
            username: this.formData.username,
            password1: this.formData.password, // dj-rest-auth는 'password1', 'password2'로 기대함
            password2: this.formData.confirmPassword,
            nickname: this.formData.nickname,
            fullname: this.formData.fullname,
          });
  
          alert("회원가입이 성공적으로 완료되었습니다!");
          this.$router.push({ name: "LoginView" });
        } catch (error) {
          console.error("회원가입 실패:", error.response?.data || error);
          alert("회원가입에 실패했습니다. 다시 시도해주세요.");
        }
      },
      goToLogin() {
        this.$router.push({ name: "LoginView" });
      },
    },
  };
  </script>
  