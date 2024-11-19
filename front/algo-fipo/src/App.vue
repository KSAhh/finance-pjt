<template>
<<<<<<< HEAD
  <div id="app" class="flex flex-col min-h-screen">
    <!-- NavBar 컴포넌트 사용 -->
    <NavBar :toggleMenu="toggleMenu" />

    <!-- 메뉴 출력 -->
    <div v-if="selectedMenu" class="w-full bg-gray-100 border border-gray-300 rounded-lg mt-2 p-4">
=======
  <div id="app" class="flex flex-col min-h-screen w-full">
    <!-- NavBar -->
    <NavBar />

    <!-- 메뉴 출력 -->
    <div
      v-if="selectedMenu"
      class="w-full bg-gray-100 border border-gray-300 rounded-lg mt-20 p-4"
    >
>>>>>>> 2cb3c18ac3b4f8614bdbfae805cf46cb95b39c17
      <p class="text-lg font-semibold text-center">
        {{ selectedMenu }} 메뉴 내용이 여기에 표시됩니다.
      </p>
    </div>

    <!-- Main Content -->
<<<<<<< HEAD
    <div class="flex-grow flex justify-center items-start">
      <router-view class="w-full"></router-view>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-100 text-center py-4 text-base lg:text-lg tracking-wide">
=======
    <div class="flex-grow flex justify-center items-start w-full mt-20">
      <router-view class="w-full max-w-screen-2xl"></router-view>
    </div>

    <!-- Footer -->
    <footer
      class="bg-gray-100 text-center py-4 text-base lg:text-lg tracking-wide"
    >
>>>>>>> 2cb3c18ac3b4f8614bdbfae805cf46cb95b39c17
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
<<<<<<< HEAD
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
=======
      selectedMenu: null,
    };
  },
};
</script>

<style>
/* 전역 스타일이 필요하면 여기에 추가 */
#app {
  position: relative;
}
</style>
>>>>>>> 2cb3c18ac3b4f8614bdbfae805cf46cb95b39c17
