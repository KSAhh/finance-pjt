<template class="min-w-[730px]">
  <div id="app" class="flex flex-col min-h-screen w-full">
    <!-- NavBar -->
    <NavBar />

    <!-- Main Content -->
    <div class="flex-grow flex justify-center items-start w-full mt-20">
      <router-view class="w-full max-w-screen-2xl"></router-view>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-100 text-center py-4 text-base lg:text-lg tracking-wide">
      우리 팀 정보
    </footer>
  </div>
</template>

<script setup>
import NavBar from "@/components/NavBar.vue";
</script>

<style scoped>
#app {
  position: relative;
}
</style>
