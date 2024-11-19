<template>
  <section class="klogin">
    <div class="kakao-login-button" @click="kakaoLoginBtn">
      카카오 로그인
    </div>
  </section>
</template>

<script>
import axios from "axios";
const KAKAO_LOGIN_JS_KEY = import.meta.env.VITE_KAKAOLOGIN_JS_KEY;
import { useNavBarStore } from "@/stores/navBarStore"; // NavBar 상태 관리 Store (Pinia 사용 시)

export default {
  name: "KLogin",

  methods: {
    async kakaoLoginBtn() {
      try {
        // Kakao 초기화
        if (!window.Kakao || !Kakao.isInitialized()) {
          Kakao.init(KAKAO_LOGIN_JS_KEY);
          console.log("Kakao SDK 초기화 완료");
        }

        // 기존 로그인 상태 초기화
        if (window.Kakao.Auth.getAccessToken()) {
          await window.Kakao.API.request({ url: "/v1/user/unlink" });
          window.Kakao.Auth.setAccessToken(undefined);
        }

        // Kakao 로그인
        window.Kakao.Auth.login({
          success: async (authObj) => {
            console.log("Kakao 인증 성공:", authObj);

            // 사용자 정보 요청
            window.Kakao.API.request({
              url: "/v2/user/me",
              data: {
                property_keys: ["kakao_account.email", "kakao_account.profile.nickname"],
              },
              success: async (response) => {
                console.log("카카오 사용자 정보:", response);

                // 사용자 정보를 백엔드로 전송
                try {
                  const serverResponse = await axios.post(
                    "http://127.0.0.1:8000/accounts/kakao/login/",
                    {
                      id: response.id,
                      email: response.kakao_account.email,
                      nickname: response.kakao_account.profile.nickname,
                    }
                  );

                  // 백엔드 응답 처리
                  const key = serverResponse.data.key; // Django 인증 토큰
                  localStorage.setItem("key", key);
                  localStorage.setItem("fullname", response.kakao_account.profile.nickname);

                  console.log("로그인 성공, 토큰 저장:", key);

                  // NavBar 상태 업데이트 (이벤트 기반)
                  const updateNavBarEvent = new Event("updateNavBar");
                  window.dispatchEvent(updateNavBarEvent);

                  // Pinia Store를 사용할 경우 (선택 사항)
                  const navBarStore = useNavBarStore();
                  navBarStore.login(response.kakao_account.profile.nickname);

                  // 메인 페이지로 리다이렉트
                  this.$router.push({ name: "MainView" });
                } catch (error) {
                  console.error("백엔드 요청 실패:", error);
                }
              },
              fail: (error) => {
                console.error("사용자 정보 요청 실패:", error);
              },
            });
          },
          fail: (error) => {
            console.error("Kakao 로그인 실패:", error);
          },
        });
      } catch (error) {
        console.error("Kakao 로그인 과정에서 오류 발생:", error);
      }
    },
  },
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
