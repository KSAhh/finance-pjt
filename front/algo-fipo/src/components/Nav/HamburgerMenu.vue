<template>
    <div class="relative group flex-shrink-0">
      <img
        src="@/assets/hamburger.svg"
        alt="menu"
        class="h-8 w-8 cursor-pointer"
      />
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
  </template>
  
  <script>
  export default {
    name: "HamburgerMenu",
  };
  </script>
  