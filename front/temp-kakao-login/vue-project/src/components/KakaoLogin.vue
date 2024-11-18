<template>
  <section class="test">
    <div v-on:click="kakaoLoginBtn">카카오 연동</div>
  </section>
  <button @click="logout">로그아웃</button>

</template>

<script>
const KAKAO_LOGIN_JS_KEY = import.meta.env.VITE_KAKAOLOGIN_JS_KEY
import axios from "axios";

export default {
  name: "test",
  methods: {
    kakaoLoginBtn: function () {
      if (!Kakao.isInitialized()) {
      Kakao.init(KAKAO_LOGIN_JS_KEY);
    }
      // window.Kakao.init(KAKAO_LOGIN_JS_KEY); // Kakao JavaScript 키

      if (window.Kakao.Auth.getAccessToken()) {
        window.Kakao.API.request({
          url: "/v1/user/unlink",
          success: function (response) {
            console.log(response);
          },
          fail: function (error) {
            console.log(error);
          },
        });
        window.Kakao.Auth.setAccessToken(undefined);
      }

      window.Kakao.Auth.login({
        success: function (authObj) {
          window.Kakao.API.request({
            url: "/v2/user/me",
            data: {
              property_keys: ["kakao_account.email", "kakao_account.profile.nickname"],
            },

            success: async function (response) {
              console.log("카카오 사용자 정보:", response);
              console.log("Kakao Login Success", authObj);

              // 사용자 정보를 백엔드로 전송
              try {
                const serverResponse = await axios.post(
                  "http://127.0.0.1:8000/accounts/kakao/login/", //{access_token:authObj.access_token},
                  {
                    id: response.id,
                    email: response.kakao_account.email,
                    nickname: response.kakao_account.profile.nickname,
                  }
                );
                console.log("백엔드 응답:", serverResponse.data);
                const key = serverResponse.data.key; // Django가 반환한 인증 토큰
                localStorage.setItem("key", key);
              } catch (error) {
                console.error("백엔드 요청 실패:", error);
              }
            },
            fail: function (error) {
              console.log(error);
            },
          });
        },
        fail: function (error) {
          console.log(error);
        },
      });
    },

    async logout() {
      try {

        // Django 로그아웃 요청
        await axios.post("http://127.0.0.1:8000/accounts/logout/", {}, {
          headers: {
            Authorization: `Token ${localStorage.getItem("key")}`,
          },
        });

        // 클라이언트에서 저장된 토큰 삭제
        console.log("Token:", localStorage.getItem("key"));

        localStorage.removeItem("key");
        axios.defaults.headers.common['Authorization'] = null;

        // 로그아웃 후 메인 페이지로 리다이렉트
        console.log("Logout successful");

        window.location.href = "/";
      } catch (error) {
        console.log(localStorage)
        console.error("Logout failed:", error.response.data);
      }
    },
  },
};
</script>

<style scoped>
.test {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
div {
  width: 200px;
  height: 40px;
  background-color: #fdd101;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
</style>


<!-- 0----------------------------------------------------- -->
<!-- <template>
  <button @click="kakaoLogin">카카오 로그인</button>
  <button @click="logout">로그아웃</button>

</template>

<script>
import axios from "axios";

export default {
  methods: {
    kakaoLogin() {
    if (!Kakao.isInitialized()) {
      Kakao.init(KAKAO_LOGIN_JS_KEY);
    }

    // 기존 세션 무효화
    if (Kakao.Auth.getAccessToken()) {
      console.log("Existing session found, logging out...");
      Kakao.Auth.logout(() => {
        console.log("Session cleared. Now opening login window...");
        this.openKakaoLogin();
      });
    } else {
      this.openKakaoLogin();
    }
  },

  // 추가????????????????????????????
  if (window.Kakao.Auth.getAccessToken()) {
        window.Kakao.API.request({
          url: "/v1/user/unlink",
          success: function (response) {
            console.log(response);
          },
          fail: function (error) {
            console.log(error);
          },
        });
        window.Kakao.Auth.setAccessToken(undefined);
      }
  // 추가????????????????????????????


  openKakaoLogin() {
    Kakao.Auth.login({
      success: (authObj) => {
        console.log("Kakao Login Success", authObj);
        this.sendTokenToServer(authObj.access_token);
      },
      fail: (err) => {
        console.error("Kakao Login Failed", err);
      },
    });
  },

  async sendTokenToServer(accessToken) {
    try {
      const response = await axios.post("http://127.0.0.1:8000/accounts/auth/kakao/login/", {
        access_token: accessToken,
      });
      const token = response.data.key;
      localStorage.setItem("authToken", token);
      axios.defaults.headers.common["Authorization"] = `Token ${token}`;
      console.log("Django Server Response:", response.data);
    } catch (error) {
      console.error("Error communicating with server:", error.response.data);
    }
  },
    // kakaoLogin() {
    //   if (!Kakao.isInitialized()) {
    //   Kakao.init(KAKAO_LOGIN_JS_KEY); // Kakao JavaScript 키
    //   }
      

    //   Kakao.Auth.login({
    //     success: (authObj) => {
    //       console.log("Kakao Login Success", authObj);
    //       this.sendTokenToServer(authObj.access_token);
    //     },
    //     fail: (err) => {
    //       console.error("Kakao Login Failed", err);
    //     },
    //   });
    // },
    // async sendTokenToServer(accessToken) {
    //   try {
    //     const response = await axios.post("http://127.0.0.1:8000/accounts/auth/kakao/login/", {
    //       access_token: accessToken,
    //     });
    //     const token = response.data.key; // Django가 반환한 인증 토큰
    //     localStorage.setItem("authToken", token); // 토큰 저장
    //     axios.defaults.headers.common['Authorization'] = `Token ${token}`; // 기본 인증 헤더 설정
    //     console.log("Django Server Response:", response.data);
    //   } catch (error) {
    //     console.error("Error communicating with server:", error.response.data);
    //   }
    // },
    async logout() {
      try {

        // Django 로그아웃 요청
        await axios.post("http://127.0.0.1:8000/accounts/logout/", {}, {
          headers: {
            Authorization: `Token ${localStorage.getItem("authToken")}`,
          },
        });

        // 클라이언트에서 저장된 토큰 삭제
        console.log("Token:", localStorage.getItem("authToken"));

        localStorage.removeItem("authToken");
        axios.defaults.headers.common['Authorization'] = null;

        // 로그아웃 후 메인 페이지로 리다이렉트
        console.log("Logout successful");

        window.location.href = "/";
      } catch (error) {
        console.log(localStorage)
        console.error("Logout failed:", error.response.data);
      }
    },
  },
};
</script> -->
<!-- 0-----------------------------------------------------
<template>
  <section class="test">
    <div v-on:click="kakaoLoginBtn">카카오 연동</div>
  </section>
</template>

<script>

export default {
  name: "test",
  methods: {
    kakaoLoginBtn:function(){

      window.Kakao.init(KAKAO_LOGIN_JS_KEY) // Kakao Developers에서 요약 정보 -> JavaScript 키

      if (window.Kakao.Auth.getAccessToken()) {
        window.Kakao.API.request({
          url: '/v1/user/unlink',
          success: function (response) {
            console.log(response)
          },
          fail: function (error) {
            console.log(error)
          },
        })
        window.Kakao.Auth.setAccessToken(undefined)
      }


      window.Kakao.Auth.login({
        success: function () {
          window.Kakao.API.request({
            url: '/v2/user/me',
            data: {
              property_keys: ["kakao_account.email"]
            },
            success: async function (response) {
              console.log(response);
            },
            fail: function (error) {
              console.log(error)
            },
          })
        },
        fail: function (error) {
          console.log(error)
        },
      })
    }
  }
}
</script>

<style scoped>
  .test{ display:flex; justify-content: center; align-items: center; height:100vh; }
  div{ width: 200px; height:40px; background-color:#fdd101; color:white; display:flex; align-items: center; justify-content: center; cursor:pointer; }
</style> -->
