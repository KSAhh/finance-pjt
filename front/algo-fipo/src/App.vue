<template class="min-w-[730px]">
  <div id="app" class="flex flex-col min-h-screen w-full">
    <!-- NavBar -->
    <NavBar v-if="shouldShowLayout" />

    <!-- Main Content -->
    <div class="flex-grow flex justify-center items-start w-full mt-20">
      <router-view class="w-full max-w-screen-2xl"></router-view>
    </div>

    <!-- Footer -->
    <footer v-if="shouldShowLayout" class="bg-gray-100 text-center py-4 text-base lg:text-lg tracking-wide">
      우리 팀 정보
    </footer>
  </div>
</template>

<script setup>
import NavBar from "@/components/NavBar.vue";
import { useRoute } from "vue-router";
import { computed } from "vue";

// 현재 라우트 가져오기
const route = useRoute();

// 특정 페이지에서 NavBar와 Footer 숨기기
const shouldShowLayout = computed(() => {
  // 레이아웃이 필요한 페이지 설정
  const noLayoutRoutes = ["/join"]; // 레이아웃을 숨길 경로
  return !noLayoutRoutes.includes(route.path);
});

</script>

<style scoped>
#app {
  position: relative;
}
</style>
