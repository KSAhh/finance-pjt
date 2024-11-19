<template>
  <li class="px-4 lg:px-6 xl:px-8 relative group">
    <!-- 메뉴 이름 -->
    <a href="#" class="hover:underline">{{ label }}</a>

    <!-- 드롭다운 메뉴 -->
    <div
      class="dropdown-menu fixed top-[64px] left-0 w-screen bg-white border border-gray-300 rounded opacity-0 h-0 overflow-hidden transition-all duration-300 group-hover:h-64 group-hover:opacity-100 z-50"
    >
      <div class="flex h-full">
        <!-- 첫 번째 영역 -->
        <div class="w-1/3 bg-gray-100 p-4">
          <h3 class="text-lg font-semibold">{{ label }} 정보</h3>
          <p class="mt-2 text-sm text-gray-600">
            {{ label }}에 대한 설명이나 관련 정보가 이 영역에 표시됩니다.
          </p>
        </div>

        <!-- 두 번째 영역 -->
        <div class="w-1/3 bg-white p-4 border-l border-r border-gray-200">
          <ul class="space-y-2">
            <li
              v-for="(item, index) in dropdownContent"
              :key="index"
              class="hover:underline cursor-pointer"
            >
              {{ item }}
            </li>
          </ul>
        </div>

        <!-- 세 번째 영역 -->
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

<script setup>
// Props 선언
defineProps({
  label: {
    type: String,
    required: true,
  },
  dropdownContent: {
    type: Array,
    default: () => [],
  },
});
</script>

<style scoped>
/* 필요 시 추가 스타일 작성 */
</style>
