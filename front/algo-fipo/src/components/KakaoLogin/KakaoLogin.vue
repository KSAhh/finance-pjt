<template>
  <section class="klogin">
    <div class="kakao-login-button" @click="kakaoLoginBtn">
      카카오 로그인
    </div>
  </section>
</template>

<script setup>
import axios from "axios";
import { useNavBarStore } from "@/stores/navBarStore"; // Pinia Store for NavBar

// Kakao JavaScript SDK Key
const KAKAO_LOGIN_JS_KEY = import.meta.env.VITE_KAKAO_LOGIN_JS_KEY;

const navBarStore = useNavBarStore();

const kakaoLoginBtn = async () => {
  try {
    // Kakao SDK Initialization
    if (!window.Kakao || !window.Kakao.isInitialized()) {
      window.Kakao.init(KAKAO_LOGIN_JS_KEY);
      console.log("Kakao SDK 초기화 완료");
    }

    // Clear Existing Login State
    if (window.Kakao.Auth.getAccessToken()) {
      await window.Kakao.API.request({ url: "/v1/user/logout" });
      window.Kakao.Auth.setAccessToken(null);
    }

    // Kakao Login Request
    window.Kakao.Auth.login({
      success: async (authObj) => {
        console.log("Kakao 인증 성공:", authObj);

        // Fetch User Information
        const response = await window.Kakao.API.request({
          url: "/v2/user/me",
          data: {
            property_keys: ["kakao_account.email", "kakao_account.profile.nickname"],
          },
        });
        console.log("카카오 사용자 정보:", response);

        // Send User Info to Backend
        const serverResponse = await axios.post("http://127.0.0.1:8000/accounts/kakao/login/", {
          id: response.id,
          email: response.kakao_account.email,
          nickname: response.kakao_account.profile.nickname,
        });
        console.log("서버 응답 데이터:", serverResponse.data);

        // Extract Token from Server Response
// 서버 응답에서 key 추출 (배열 또는 단일 객체 처리)
const key = Array.isArray(serverResponse.data.key)
  ? serverResponse.data.key[0]?.key // 배열인 경우 첫 번째 요소의 key
  : serverResponse.data.key; // 단일 객체인 경우 직접 key

if (!key) {
  throw new Error("서버 응답에 key가 없습니다.");
}


        // Store Token and Full Name in Local Storage
        localStorage.setItem("key", key);
        localStorage.setItem("fullname", response.kakao_account.profile.nickname);

        // Set Axios Authorization Header
        axios.defaults.headers.common["Authorization"] = `Token ${key}`;
        console.log("로그인 성공, 토큰 저장:", key);

        // Update Pinia Store
        navBarStore.login(response.kakao_account.profile.nickname);

        // Redirect to Main Page
        window.location.href = "/";
      },
      fail: (error) => {
        console.error("Kakao 로그인 실패:", error);
      },
    });
  } catch (error) {
    console.error("Kakao 로그인 과정에서 오류 발생:", error);
  }
  
};

</script>

<style scoped>
.kakao-login-button {
  background-color: #fee500;
  color: rgba(0, 0, 0, 0.51);
  border: 1px solid lightgray;
  padding: 0.5rem 0;
  border-radius: 0.25rem;
  font-weight: bold;
  text-align: center;
  cursor: pointer;
}

.kakao-login-button:hover {
  background-color: #ffd700;
}
</style>
