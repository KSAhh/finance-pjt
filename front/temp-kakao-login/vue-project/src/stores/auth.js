import { defineStore } from "pinia";
import axios from "axios";

const KAKAO_LOGIN_JS_KEY=VITE_KAKAOLOGIN_JS_KEY
export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("authToken") || null, // 초기 토큰 로드
  }),
  actions: {
    async loginWithKakao(kakaoAccessToken) {
      try {
        // Kakao Access Token을 Django로 전송
        const response = await axios.post(
          "http://127.0.0.1:8000/accounts/kakao/login/callback/", // Django Callback URL
          {
            access_token: kakaoAccessToken, // Kakao에서 받은 Access Token
          }
        );

        // Django가 반환한 인증 토큰 저장
        const token = response.data.key; // Django 서버에서 반환하는 토큰 (JWT 또는 DRF Token)
        this.token = token;

        // 로컬 스토리지 및 Axios 기본 헤더에 토큰 저장
        localStorage.setItem("authToken", token);
        axios.defaults.headers.common["Authorization"] = `Token ${token}`;
        console.log("Login successful, token stored.");
      } catch (error) {
        console.error("Login failed:", error.response?.data || error);
        this.token = null;
      }
    },
  },
});
