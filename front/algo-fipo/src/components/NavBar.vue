<template>
    
    <nav class="bg-white shadow py-4 px-6 flex justify-between items-center w-full gap-4 relative">
      <!-- 로고 -->
      <div class="ml-4 md:ml-8 lg:ml-16 xl:ml-48 2xl:ml-56">
        <img src="@/assets/headerlogo.svg" alt="logo" class="h-8 sm:h-10 md:h-12 lg:h-14" />
      </div>
  
      <!-- 기본 메뉴 -->
      <ul class="hidden sm:flex text-sm sm:text-base md:text-lg lg:text-xl tracking-wide whitespace-nowrap">
        <li class="px-2 md:px-4 lg:px-6 xl:px-8 relative group">
          <a href="#" class="hover:underline">예적금</a>
          <div
            class="absolute top-full left-0 bg-white border border-gray-300 rounded opacity-0 w-0 h-0 transition-all duration-300 group-hover:w-full group-hover:h-32 group-hover:opacity-100"
          >
            <p class="p-4 text-sm sm:text-base">예적금 메뉴 내용</p>
          </div>
        </li>
        <li class="px-2 md:px-4 lg:px-6 xl:px-8 relative group">
          <a href="#" class="hover:underline">대출</a>
          <div
            class="absolute top-full left-0 bg-white border border-gray-300 rounded opacity-0 w-0 h-0 transition-all duration-300 group-hover:w-full group-hover:h-32 group-hover:opacity-100"
          >
            <p class="p-4 text-sm sm:text-base">대출 메뉴 내용</p>
          </div>
        </li>
        <li class="px-2 md:px-4 lg:px-6 xl:px-8 relative group">
          <a href="#" class="hover:underline">외화예적금</a>
          <div
            class="absolute top-full left-0 bg-white border border-gray-300 rounded opacity-0 w-0 h-0 transition-all duration-300 group-hover:w-full group-hover:h-32 group-hover:opacity-100"
          >
            <p class="p-4 text-sm sm:text-base">외화예적금 메뉴 내용</p>
          </div>
        </li>
        <li class="px-2 md:px-4 lg:px-6 xl:px-8 relative group">
          <a href="#" class="hover:underline">환율</a>
          <div
            class="absolute top-full left-0 bg-white border border-gray-300 rounded opacity-0 w-0 h-0 transition-all duration-300 group-hover:w-full group-hover:h-32 group-hover:opacity-100"
          >
            <p class="p-4 text-sm sm:text-base">환율 메뉴 내용</p>
          </div>
        </li>
      </ul>
  
      <!-- 버튼 -->
      <div class="flex items-center space-x-4 mr-4 md:mr-8 lg:mr-16 xl:mr-64 2xl:mr-80 relative">
        <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 min-w-[100px]">
          로그인
        </button>
        <button class="bg-gray-200 text-black px-4 py-2 rounded hover:bg-gray-300 min-w-[100px]">
          회원가입
        </button>
        <!-- = 버튼 -->
        <div class="relative group">
          <img
            src="@/assets/hamburger.svg"
            alt="menu"
            class="h-6 cursor-pointer md:h-8"
          />
          <!-- = 버튼 호버 시 출력 메뉴 -->
          <div
            class="absolute top-full left-0 bg-white border border-gray-300 rounded opacity-0 w-0 h-0 transition-all duration-300 group-hover:w-full group-hover:h-32 group-hover:opacity-100"
          >
            <ul>
              <li class="hover:bg-gray-100">예적금</li>
              <li class="px-4 py-2 hover:bg-gray-100">대출</li>
              <li class="px-4 py-2 hover:bg-gray-100">외화예적금</li>
              <li class="px-4 py-2 hover:bg-gray-100">환율</li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: "NavBar",
  };
  </script>
  
  <style scoped>
  /* 애니메이션 효과 */
  .group-hover\:w-full:hover {
    width: 100%;
  }
  .group-hover\:h-32:hover {
    height: 8rem;
  }
  .group-hover\:opacity-100:hover {
    opacity: 1;
  }
  </style>
  