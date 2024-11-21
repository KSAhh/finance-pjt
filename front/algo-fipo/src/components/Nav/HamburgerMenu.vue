<template>
  <div class="relative group flex-shrink-0">
    <!-- 햄버거 아이콘 -->
    <img
      src="@/assets/hamburger.svg"
      alt="menu"
      class="h-8 w-8 cursor-pointer"
    />
    
    <!-- 드롭다운 메뉴 -->
    <div
      class="absolute top-full right-0 bg-white border border-gray-300 rounded opacity-0 w-40 h-0 transition-all duration-300 group-hover:h-40 group-hover:opacity-100 overflow-hidden"
    >
      <ul class="flex flex-col">
        <li 
          v-for="(item, index) in menuItems" 
          :key="index" 
          class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
          @click="goToMyPage(item)">
          {{ item }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router"; // 라우터 사용

const router = useRouter(); // Vue Router 인스턴스 가져오기

// 메뉴 항목 데이터
const menuItems = ref(["마이페이지", "자주하는 질문", "고객센터", "임시"]);

// 클릭 핸들러
const goToMyPage = (item) => {
  if (item === "마이페이지") {
    router.push({ name: "MyPage" });
  } else if (item === "자주하는 질문") {
    router.push({ name: "FAQ" }); // 필요 시 다른 라우터 추가
  } else if (item === "고객센터") {
    router.push({ name: "CustomerSupport" });
  }
};
</script>

<style scoped>
/* 필요 시 추가 스타일 작성 */
</style>
