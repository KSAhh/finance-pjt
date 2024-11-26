<template>
  <div>
    <p>로그인 중...</p>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();

// 현재 URL에서 code 추출
const urlParams = new URLSearchParams(window.location.search);
const code = urlParams.get("code");

const processLogin = async () => {
  try {
    const response = await axios.post("http://localhost:8000/accounts/social/kakao/login/", {
      code,
    });
    
    const token = response.data.token;
    if (!token) {
      throw new Error("서버에서 토큰을 받아오지 못했습니다.");
    }

    // 토큰 저장
    localStorage.setItem("key", token);
    alert("로그인 성공!");

    // 메인 페이지로 이동
    router.push("/");
  } catch (error) {
    console.error("로그인 실패:", error);
    alert("로그인에 실패했습니다. 다시 시도해주세요.");
  }
};

// 로그인 처리 시작
processLogin();
</script>
