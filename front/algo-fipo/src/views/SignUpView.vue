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
        <router-link to="/login" class="hover:underline">
          이미 계정이 있으신가요?
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router"; // useRouter를 가져옵니다.

const router = useRouter(); // useRouter 훅 사용
const formData = ref({
  username: "",
  password: "",
  confirmPassword: "",
  nickname: "",
  fullname: "",
});

const preventUndo = (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "z") {
    event.preventDefault();
  }
};

const signup = async () => {
  if (formData.value.password !== formData.value.confirmPassword) {
    alert("비밀번호가 일치하지 않습니다.");
    return;
  }

  if (!formData.value.username || !formData.value.nickname || !formData.value.fullname) {
    alert("모든 필드를 채워주세요.");
    return;
  }

  if (formData.value.password.length < 8) {
    alert("비밀번호는 최소 8자 이상이어야 합니다.");
    return;
  }

  try {
    const response = await axios.post("http://127.0.0.1:8000/accounts/signup/", {
      username: formData.value.username,
      password1: formData.value.password,
      password2: formData.value.confirmPassword,
      nickname: formData.value.nickname,
      fullname: formData.value.fullname,
    });

    const token = response.data.key;
    if (token) {
      localStorage.setItem("key", token);
      localStorage.setItem("fullname", formData.value.fullname);
      axios.defaults.headers.common["Authorization"] = `Token ${token}`;
      alert("회원가입이 성공적으로 완료되었습니다!");
      router.push({ name: "MainView" }); // router.push로 라우팅
    } else {
      alert("회원가입은 완료되었으나 자동 로그인을 처리할 수 없습니다.");
    }
  } catch (error) {
    console.error("회원가입 실패:", error.response?.data || error);
    const errorMessage = error.response?.data?.detail || "회원가입에 실패했습니다. 다시 시도해주세요.";
    alert(errorMessage);
  } finally {
    formData.value = {
      username: "",
      password: "",
      confirmPassword: "",
      nickname: "",
      fullname: "",
    };
  }
};
</script>


<style scoped>
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
