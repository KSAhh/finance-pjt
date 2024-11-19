<template>
  <div id="app" class="flex flex-col min-h-screen w-full">
    <!-- NavBar -->
    <NavBar />

    <!-- 메뉴 출력 -->
    <div
      v-if="selectedMenu"
      class="w-full bg-gray-100 border border-gray-300 rounded-lg mt-20 p-4"
    >
      <p class="text-lg font-semibold text-center">
        {{ selectedMenu }} 메뉴 내용이 여기에 표시됩니다.
      </p>
    </div>

    <!-- Main Content -->
    <div class="flex-grow flex justify-center items-start w-full mt-20">
      <router-view class="w-full max-w-screen-2xl"></router-view>
    </div>

    <!-- Footer -->
    <footer
      class="bg-gray-100 text-center py-4 text-base lg:text-lg tracking-wide"
    >
      우리 팀 정보
    </footer>
  </div>
</template>

<script setup>
import { ref } from "vue";
import NavBar from "@/components/NavBar.vue";

// 상태 관리
const selectedMenu = ref(null);
</script>

<style scoped>
/* 전역 스타일이 필요하면 여기에 추가 */
#app {
  position: relative;
}
</style>
