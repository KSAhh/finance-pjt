<template>
  <button @click="logout" class="logout-button">
    로그아웃
  </button>
</template>

<script>
import axios from "axios";

export default {
  name: "LogoutButton",
  methods: {
    async loadKakaoSDK() {
      return new Promise((resolve, reject) => {
        if (window.Kakao) {
          resolve(window.Kakao);
        } else {
          const script = document.createElement('script');
          script.src = 'https://developers.kakao.com/sdk/js/kakao.min.js';
          script.onload = () => {
            if (window.Kakao) {
              resolve(window.Kakao);
            } else {
              reject(new Error('Kakao SDK failed to load'));
            }
          };
          script.onerror = () => reject(new Error('Kakao SDK failed to load'));
          document.head.appendChild(script);
        }
      });
    },
    async initializeKakao() {
      const Kakao = await this.loadKakaoSDK();
      if (!Kakao.isInitialized()) {
        Kakao.init(import.meta.env.VITE_KAKAOLOGIN_JS_KEY); // Ensure the key is correct
        console.log('Kakao SDK initialized');
      }
      return Kakao;
    },
    async logout() {
  try {
    const Kakao = await this.initializeKakao();
    if (Kakao.Auth.getAccessToken()) {
      await Kakao.API.request({ url: "/v1/user/logout" });
      console.log("카카오 로그아웃 성공");
    }
  } catch (error) {
    console.error("Kakao logout failed:", error);
  }

  try {
    const token = localStorage.getItem("key");
    if (token) {
      await axios.post("http://127.0.0.1:8000/accounts/logout/", {}, {
        headers: { Authorization: `Token ${token}` },
      });
      console.log("Django 로그아웃 성공");
    }
  } catch (error) {
    console.error("Django logout failed:", error);
  }

  // 로컬 스토리지 데이터 제거
  localStorage.removeItem("key");
  localStorage.removeItem("fullname");
  localStorage.clear(); // Alternatively, check all related keys explicitly


  // NavBar 업데이트 이벤트 트리거
  const updateNavBarEvent = new Event("updateNavBar");
  window.dispatchEvent(updateNavBarEvent);

  // 리다이렉트
  window.location.href = "/";
}}}

</script>

<style scoped>
.logout-button {
  background-color: #ff6b6b;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
}
.logout-button:hover {
  background-color: #e63946;
}
</style>
