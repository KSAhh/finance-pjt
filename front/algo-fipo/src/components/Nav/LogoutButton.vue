<template>
  <button @click="logout" class="logout-button">로그아웃</button>
</template>

<script setup>
import { useRouter, useRoute } from "vue-router"; // vue-router에서 router와 route 가져오기
import { useNavBarStore } from "@/stores/navBarStore";

const navBarStore = useNavBarStore();
const router = useRouter();
const route = useRoute(); // 현재 라우트 정보 가져오기

const logout = async () => {
  try {
    await navBarStore.logout(); // 로그아웃 처리
    console.log("로그아웃 완료");

    // 현재 경로에 meta.requiresAuth가 설정되어 있는 경우에만 메인 페이지로 리다이렉트
    if (route.meta.requiresAuth) {
      router.push({ name: "MainView" });
    }
  } catch (error) {
    console.error("로그아웃 실패:", error);
  }
};
</script>

<style scoped>
.logout-button {
  display: inline-flex;
  align-items: center;
  background-color: white; /* 화려한 레드 색상 */
  color: black;
  font-size: 0.8rem;
  font-weight: bold;
  padding: 0.75rem 1rem;
  border: 1px;
  border-radius: 0.5rem;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0.1, 0.1, 0.1, 0.1);
  transition: background-color 0.3s ease;
}

.logout-button:hover {
  background-color: black; 
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
  color: white;
}

.logout-button:active {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

</style>