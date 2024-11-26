<template>
  <nav class="bg-white shadow py-4 px-6 flex justify-between items-center w-full fixed top-0 left-0 z-50 whitespace-nowrap">
    <!-- Logo -->
    <div class="flex-shrink-0">
      <router-link to="/" class="flex items-center">
        <Logo />
      </router-link>
    </div>

    <!-- Main Menu -->
    <div class="flex-grow hidden sm:flex justify-center items-center space-x-4">
      <Menu />
    </div>

    <!-- User Status-based Menu -->
    <div class="flex items-center space-x-4 mr-4">
      <template v-if="isLoggedIn">
        <span class="text-gray-600">{{ navBarStore.userNickname }}</span>
        <LogoutButton />
      </template>
      <template v-else>
        <LoginButton />
        <SignUpButton />
      </template>
    </div>

    <!-- 햄버거 메뉴 -->
    <div class="absolute right-4 top-4 sm:static">
      <HamburgerMenu class="w-8 h-8 " />
    </div>
  </nav>
</template>

<script setup>
import { useNavBarStore } from "@/stores/navBarStore"
import { computed, onMounted, watchEffect, ref  } from "vue";
import Logo from "./Nav/Logo.vue";
import Menu from "./Nav/Menu.vue";
import LoginButton from "./Nav/LoginButton.vue";
import SignUpButton from "./Nav/SignUpButton.vue";
import HamburgerMenu from "./Nav/HamburgerMenu.vue";
import LogoutButton from "./Nav/LogoutButton.vue";

const navBarStore = useNavBarStore()
const isLoggedIn = computed(() => navBarStore.isLoggedIn)
const nickname = ref(localStorage.getItem('nickname'))
nickname.value = computed(() => localStorage.getItem('nickname'))
nickname.value = computed(() => navBarStore.nickname)

</script>

