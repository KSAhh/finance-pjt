
<template>
  <nav class="bg-white shadow py-4 px-6 flex justify-between items-center w-full fixed top-0 left-0 z-50">
    <!-- Logo -->
    <Logo @click="goToMain" />

    <!-- Main Menu -->
    <Menu />

    <!-- User Status-based Menu -->
    <div class="flex items-center space-x-4 mr-4">
      <template v-if="navBarStore.isLoggedIn">
        <span v-if="navBarStore.userFullName" class="text-gray-600">{{ navBarStore.userFullName }}</span>
        <LogoutButton />
      </template>
      <template v-else>
        <LoginButton />
        <SignUpButton />
      </template>
      <HamburgerMenu />
    </div>
  </nav>
</template>

  <script setup>
  import { onMounted, onUnmounted } from "vue";
  import { useNavBarStore } from "@/stores/navBarStore";
  import Logo from "./Nav/Logo.vue";
  import Menu from "./Nav/Menu.vue";
  import LoginButton from "./Nav/LoginButton.vue";
  import SignUpButton from "./Nav/SignUpButton.vue";
  import HamburgerMenu from "./Nav/HamburgerMenu.vue";
  import LogoutButton from "./Nav/LogoutButton.vue";
  
  const navBarStore = useNavBarStore();
  
  onMounted(() => {
    const updateNavBar = () => {
      navBarStore.isLoggedIn = !!localStorage.getItem("key");
      navBarStore.userFullName = localStorage.getItem("fullname") || "";
    };
  
    // 이벤트 리스너 등록
    window.addEventListener("updateNavBar", updateNavBar);
  
    // 초기 상태 설정
    updateNavBar();
  });
  
  onUnmounted(() => {
    // 이벤트 리스너 해제
    window.removeEventListener("updateNavBar", updateNavBar);
  });
  </script>
<style scoped>
/* 필요한 경우 스타일 추가 */
</style>
