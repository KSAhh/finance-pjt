// auth.js
import { defineStore } from "pinia";
import axios from "axios";

const KAKAO_LOGIN_JS_KEY = import.meta.env.VITE_KAKAOLOGIN_JS_KEY;

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("key") || null, // Use consistent key name
  }),
  actions: {
    async loginWithKakao(kakaoAccessToken) {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/accounts/kakao/login/callback/",
          {
            access_token: kakaoAccessToken,
          }
        );

        console.log('Response data from Kakao login:', response.data);

        // Correctly extract the token string
        const token = response.data.key && response.data.key[0] && response.data.key[0].key;
        if (!token) {
          throw new Error("Token not found in Kakao login response");
        }

        this.token = token;

        // Store the token string, not an object
        localStorage.setItem("key", token);
        axios.defaults.headers.common["Authorization"] = `Token ${token}`;
        console.log("Login successful, token stored.");
        
        // Emit event to update NavBar
        const updateNavBarEvent = new Event("updateNavBar");
        window.dispatchEvent(updateNavBarEvent);
      } catch (error) {
        console.error("Login failed:", error.response?.data || error);
        this.token = null;
      }
    },
  },
});
