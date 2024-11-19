<template>
    <li class="px-4 lg:px-6 xl:px-8 relative group">
      <a href="#" class="hover:underline">{{ label }}</a>
      <div
        class="dropdown-menu fixed top-[64px] left-0 w-screen bg-white border border-gray-300 rounded opacity-0 h-0 overflow-hidden transition-all duration-300 group-hover:h-64 group-hover:opacity-100 z-50"
      >
        <div class="flex h-full">
          <div class="w-1/3 bg-gray-100 p-4">
            <h3 class="text-lg font-semibold">{{ label }} 정보</h3>
            <p class="mt-2 text-sm text-gray-600">
              {{ label }}에 대한 설명이나 관련 정보가 이 영역에 표시됩니다.
            </p>
          </div>
          <div class="w-1/3 bg-white p-4 border-l border-r border-gray-200">
            <ul class="space-y-2">
              <li v-for="(item, index) in dropdownContent" :key="index" class="hover:underline cursor-pointer">
                {{ item }}
              </li>
            </ul>
          </div>
          <div class="w-1/3 bg-gray-100 p-4">
            <h3 class="text-lg font-semibold">추가 정보</h3>
            <p class="mt-2 text-sm text-gray-600">
              {{ label }}과 관련된 추가 정보가 표시될 수 있습니다.
            </p>
          </div>
        </div>
      </div>
    </li>
  </template>
  
  <script>
  export default {
    name: "MenuItem",
    props: {
      label: String,
      dropdownContent: Array,
    },
  };
  </script>
  