<template>
  <div>
    <p>로그인 중...</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  async mounted() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get("code");

    try {
      const response = await axios.post("http://localhost:8000/accounts/social/kakao/login/", {
        code: code,
      });

      localStorage.setItem("token", response.data.token);
      alert("로그인 성공!");
      this.$router.push("/"); // 로그인 후 메인 페이지로 리다이렉트
    } catch (error) {
      console.error("로그인 실패:", error);
    }
  },
};
</script>
