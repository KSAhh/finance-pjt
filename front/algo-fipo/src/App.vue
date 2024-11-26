<template class="min-w-[730px]">
  <div id="app" class="flex flex-col min-h-screen w-full">
    <!-- NavBar -->
    <NavBar v-if="shouldShowLayout" />

    <!-- Main Content -->
    <div class="flex-grow flex justify-center items-start w-full mt-20">
      <router-view class="w-full max-w-screen-2xl"></router-view>
    </div>

    <!-- Footer -->
    <!-- 여기에 Foot 컴포넌트 넣는법 -->
    <Foot />
  </div>
</template>

<script setup>
import NavBar from "@/components/NavBar.vue";
import { useRoute } from "vue-router";
import { computed } from "vue"
import Foot from "./components/Foot.vue";

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
