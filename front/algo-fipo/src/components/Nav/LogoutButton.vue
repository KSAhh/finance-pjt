<template>
  <button @click="logout" class="logout-button">로그아웃</button>
</template>

<script setup>
import { useNavBarStore } from "@/stores/navBarStore";

const navBarStore = useNavBarStore();

const logout = async () => {
  try {
    await navBarStore.logout(); // Pinia 스토어의 logout 호출
    console.log("로그아웃 완료");
  } catch (error) {
    console.error("로그아웃 실패:", error);
  }
};
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
