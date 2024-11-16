<!-- <template>
  <div>
    <button @click="kakaoLogin">카카오 로그인</button>
  </div>
</template>

<script>
export default {
  methods: {
    kakaoLogin() {
      Kakao.Auth.authorize({
        redirectUri: "http://127.0.0.1:8000/accounts/kakao/login/callback/",
      });
    },
  },
};
</script> -->

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

      window.Kakao.init('6e33878e81763bd25687a8455324f354') // Kakao Developers에서 요약 정보 -> JavaScript 키

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
</style>