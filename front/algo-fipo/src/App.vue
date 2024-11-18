<template>
  <div id="app" class="flex flex-col min-h-screen">
    <!-- NavBar 컴포넌트 사용 -->
    <NavBar :toggleMenu="toggleMenu" />

    <!-- 메뉴 출력 -->
    <div v-if="selectedMenu" class="w-full bg-gray-100 border border-gray-300 rounded-lg mt-2 p-4">
      <p class="text-lg font-semibold text-center">
        {{ selectedMenu }} 메뉴 내용이 여기에 표시됩니다.
      </p>
    </div>

    <!-- Main Content -->
    <div class="flex-grow flex justify-center items-start">
      <router-view class="w-full"></router-view>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-100 text-center py-4 text-base lg:text-lg tracking-wide">
      우리 팀 정보
    </footer>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
  data() {
    return {
      selectedMenu: null, // 현재 선택된 메뉴
    };
  },
  methods: {
    toggleMenu(menu) {
      this.selectedMenu = menu; // 메뉴를 클릭하면 상태 업데이트
    },
  },
};
</script>
