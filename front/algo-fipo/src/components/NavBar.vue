<template>
  <nav
    class="bg-white shadow py-4 px-6 flex justify-between items-center w-full fixed top-0 left-0 z-50"
  >
    <!-- Logo -->
    <Logo @click="goToMain" />

    <!-- Main Menu -->
    <Menu />

    <!-- User Status-based Menu -->
    <div class="flex items-center space-x-4 mr-4">
      <template v-if="isLoggedIn">
        <span v-if="userFullName" class="text-gray-600">{{ userFullName }}</span>
        <LogoutButton />
      </template>
      <template v-else>
        <LoginButton @click="goToLogin" />
        <SignUpButton />
      </template>
      <HamburgerMenu />
    </div>
  </nav>
</template>

<script>
import axios from "axios";
import Logo from "./Nav/Logo.vue";
import Menu from "./Nav/Menu.vue";
import LoginButton from "./Nav/LoginButton.vue";
import SignUpButton from "./Nav/SignUpButton.vue";
import HamburgerMenu from "./Nav/HamburgerMenu.vue";
import LogoutButton from "./Nav/LogoutButton.vue";

export default {
  name: "NavBar",
  components: {
    Logo,
    Menu,
    LoginButton,
    SignUpButton,
    HamburgerMenu,
    LogoutButton,
  },
  data() {
    return {
      isLoggedIn: false,
      userFullName: "",
    };
  },
  methods: {
    goToMain() {
      this.$router.push({ name: "MainView" });
    },
    goToLogin() {
      this.$router.push({ name: "LoginView" });
    },
    async fetchFullName() {
      try {
        const token = localStorage.getItem("key");
        console.log('Token from localStorage:', token); // Should log the token string
        if (!token) {
          throw new Error("Token not found in localStorage");
        }
        const response = await axios.get("http://127.0.0.1:8000/accounts/user/", {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        this.userFullName = response.data.fullname;
      } catch (error) {
        console.error("fullname 가져오기 실패:", error.response?.data || error);
        this.userFullName = "";
      }
    },
    checkLoginStatus() {
      const token = localStorage.getItem("key");
      if (token) {
        this.isLoggedIn = true;
        this.fetchFullName();
      } else {
        this.isLoggedIn = false;
        this.userFullName = "";
      }
    },
  },
  mounted() {
    console.log("NavBar mounted: 로그인 상태 확인");
    this.checkLoginStatus();

    // Add event listener for login/logout updates
    window.addEventListener("updateNavBar", this.checkLoginStatus);
  },
  beforeUnmount() {
    // Remove event listener
    window.removeEventListener("updateNavBar", this.checkLoginStatus);
  },
};
</script>