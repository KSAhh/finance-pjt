<template>
<<<<<<< HEAD
    
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
  
=======
  <nav
    class="bg-white shadow py-4 px-6 flex justify-between items-center w-full fixed top-0 left-0 z-50"
  >
   <!-- 로고 -->
   <div class="ml-8 flex-shrink-0 cursor-pointer" @click="goToMain">
      <img src="@/assets/headerlogo.svg" alt="logo" class="h-12 w-auto" />
    </div>
    <!-- 기본 메뉴 -->
    <ul
      class="hidden sm:flex text-base md:text-lg lg:text-xl tracking-wide whitespace-nowrap"
    >
      <!-- 예적금 메뉴 -->
      <li class="px-4 lg:px-6 xl:px-8 relative group">
        <a href="#" class="hover:underline">예적금</a>
        <div
          class="dropdown-menu fixed top-[64px] left-0 w-screen bg-white border border-gray-300 rounded opacity-0 h-0 overflow-hidden transition-all duration-300 group-hover:h-64 group-hover:opacity-100 z-50"
        >
          <div class="flex h-full">
            <div class="w-1/3 bg-gray-100 p-4">
              <h3 class="text-lg font-semibold">예적금 정보</h3>
              <p class="mt-2 text-sm text-gray-600">
                예적금에 대한 상세한 설명이나 관련 정보가 이 영역에 표시됩니다.
              </p>
            </div>
            <div class="w-1/3 bg-white p-4 border-l border-r border-gray-200">
              <ul class="space-y-2">
                <li class="hover:underline cursor-pointer">예적금 상품 1</li>
                <li class="hover:underline cursor-pointer">예적금 상품 2</li>
                <li class="hover:underline cursor-pointer">예적금 상품 3</li>
              </ul>
            </div>
            <div class="w-1/3 bg-gray-100 p-4">
              <h3 class="text-lg font-semibold">추가 정보</h3>
              <p class="mt-2 text-sm text-gray-600">
                예적금과 관련된 추가 정보가 표시될 수 있습니다.
              </p>
            </div>
          </div>
        </div>
      </li>

      <!-- 대출 메뉴 -->
      <li class="px-4 lg:px-6 xl:px-8 relative group">
        <a href="#" class="hover:underline">대출</a>
        <div
          class="dropdown-menu fixed top-[64px] left-0 w-screen bg-white border border-gray-300 rounded opacity-0 h-0 overflow-hidden transition-all duration-300 group-hover:h-64 group-hover:opacity-100 z-50"
        >
          <div class="flex h-full">
            <div class="w-1/3 bg-gray-100 p-4">
              <h3 class="text-lg font-semibold">대출 정보</h3>
              <p class="mt-2 text-sm text-gray-600">
                대출에 대한 상세한 설명이나 관련 정보가 표시됩니다.
              </p>
            </div>
            <div class="w-1/3 bg-white p-4 border-l border-r border-gray-200">
              <ul class="space-y-2">
                <li class="hover:underline cursor-pointer">대출 상품 1</li>
                <li class="hover:underline cursor-pointer">대출 상품 2</li>
                <li class="hover:underline cursor-pointer">대출 상품 3</li>
              </ul>
            </div>
            <div class="w-1/3 bg-gray-100 p-4">
              <h3 class="text-lg font-semibold">추가 정보</h3>
              <p class="mt-2 text-sm text-gray-600">
                대출과 관련된 추가 정보가 표시될 수 있습니다.
              </p>
            </div>
          </div>
        </div>
      </li>

      <!-- 외화예적금 메뉴 -->
      <li class="px-4 lg:px-6 xl:px-8 relative group">
        <a href="#" class="hover:underline">외화예적금</a>
        <div
          class="dropdown-menu fixed top-[64px] left-0 w-screen bg-white border border-gray-300 rounded opacity-0 h-0 overflow-hidden transition-all duration-300 group-hover:h-64 group-hover:opacity-100 z-50"
        >
          <div class="flex h-full">
            <div class="w-1/3 bg-gray-100 p-4">
              <h3 class="text-lg font-semibold">외화예적금 정보</h3>
              <p class="mt-2 text-sm text-gray-600">
                외화예적금에 대한 설명이나 관련 정보가 이 영역에 표시됩니다.
              </p>
            </div>
            <div class="w-1/3 bg-white p-4 border-l border-r border-gray-200">
              <ul class="space-y-2">
                <li class="hover:underline cursor-pointer">외화예적금 상품 1</li>
                <li class="hover:underline cursor-pointer">외화예적금 상품 2</li>
                <li class="hover:underline cursor-pointer">외화예적금 상품 3</li>
              </ul>
            </div>
            <div class="w-1/3 bg-gray-100 p-4">
              <h3 class="text-lg font-semibold">추가 정보</h3>
              <p class="mt-2 text-sm text-gray-600">
                외화예적금과 관련된 추가 정보가 표시될 수 있습니다.
              </p>
            </div>
          </div>
        </div>
      </li>

      <!-- 환율 메뉴 -->
      <li class="px-4 lg:px-6 xl:px-8 relative group">
        <a href="#" class="hover:underline">환율</a>
        <div
          class="dropdown-menu fixed top-[64px] left-0 w-screen bg-white border border-gray-300 rounded opacity-0 h-0 overflow-hidden transition-all duration-300 group-hover:h-64 group-hover:opacity-100 z-50"
        >
          <div class="flex h-full">
            <div class="w-1/3 bg-gray-100 p-4">
              <h3 class="text-lg font-semibold">환율 정보</h3>
              <p class="mt-2 text-sm text-gray-600">
                환율에 대한 설명이나 관련 정보가 이 영역에 표시됩니다.
              </p>
            </div>
            <div class="w-1/3 bg-white p-4 border-l border-r border-gray-200">
              <ul class="space-y-2">
                <li class="hover:underline cursor-pointer">환율 상품 1</li>
                <li class="hover:underline cursor-pointer">환율 상품 2</li>
                <li class="hover:underline cursor-pointer">환율 상품 3</li>
              </ul>
            </div>
            <div class="w-1/3 bg-gray-100 p-4">
              <h3 class="text-lg font-semibold">추가 정보</h3>
              <p class="mt-2 text-sm text-gray-600">
                환율과 관련된 추가 정보가 표시될 수 있습니다.
              </p>
            </div>
          </div>
        </div>
      </li>
    </ul>

    <!-- 로그인/회원가입 버튼 -->
    <div class="flex items-center space-x-4 mr-4">
      <button
        @click="goToLogin"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 whitespace-nowrap"
      >
        로그인
      </button>
      <button
        class="bg-gray-200 text-black px-4 py-2 rounded hover:bg-gray-300 whitespace-nowrap"
      >
        회원가입
      </button>
    <!-- 햄버거 아이콘 -->
    <div class="relative group flex-shrink-0">
        <img
          src="@/assets/hamburger.svg"
          alt="menu"
          class="h-8 w-8 cursor-pointer"
        />
        <!-- 햄버거 메뉴 -->
        <div
          class="absolute top-full right-0 bg-white border border-gray-300 rounded opacity-0 w-40 h-0 transition-all duration-300 group-hover:h-40 group-hover:opacity-100 overflow-hidden"
        >
          <ul class="flex flex-col">
            <li class="px-4 py-2 hover:bg-gray-100">예적금</li>
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
  methods: {
    goToMain() {
      this.$router.push({ name: "MainView" }); // MainView로 이동
    },
    goToLogin() {
      this.$router.push({ name: "LoginView" }); // LoginView로 이동
    },
  },
};
</script>

<style scoped>
/* 드롭다운 초기 상태 */
.dropdown-menu {
  transform: translateY(16px); /* 초기 위치 */
  transition: all 0.3s ease; /* 부드러운 애니메이션 */
}

/* 드롭다운 활성화 상태 */
.group:hover .dropdown-menu {
  transform: translateY(16px); /* 아래로 펼쳐짐 */
}

/* 드롭다운 내부 스타일 */
.dropdown-menu .flex {
  display: flex;
  height: 100%; /* 드롭다운 전체 높이 */
}
</style>
>>>>>>> 2cb3c18ac3b4f8614bdbfae805cf46cb95b39c17
