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
      console.log("기존 액세스 토큰이 감지됨:", window.Kakao.Auth.getAccessToken());

      // 강제 로그아웃
      try {
        await window.Kakao.API.request({ url: "/v1/user/logout" });
        console.log("카카오 로그아웃 성공");
      } catch (logoutError) {
        console.error("카카오 로그아웃 요청 실패:", logoutError);
      }

      // 모든 세션 데이터 초기화
      window.Kakao.Auth.setAccessToken(null);
      localStorage.removeItem("kakao_access_token"); // 필요 시 추가
      console.log("카카오 세션 데이터 초기화 완료");
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
        const key = Array.isArray(serverResponse.data.key)
          ? serverResponse.data.key[0]?.key
          : serverResponse.data.key;

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
    // 오류 발생 시 세션 데이터 초기화
    localStorage.removeItem("key");
    localStorage.removeItem("fullname");
    window.Kakao.Auth.setAccessToken(null);
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
