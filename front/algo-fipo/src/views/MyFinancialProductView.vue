<template>
    <div class="container mx-auto px-4 py-8">
      <!-- 제목 -->
      <h1 class="text-4xl font-bold mb-8">내 금융상품</h1>
      
      <!-- 금융상품 리스트 -->
      <div class="grid grid-cols-3 gap-8 border-b pb-6">
        <div>
          <h2 class="text-2xl font-semibold mb-4">예금</h2>
          <ul class="divide-y divide-gray-300">
            <li
              v-for="(item, index) in depositItems"
              :key="index"
              class="py-2 text-sm"
            >
              {{ item }}
            </li>
          </ul>
        </div>
        <div>
          <h2 class="text-2xl font-semibold mb-4">적금</h2>
          <ul class="divide-y divide-gray-300">
            <li
              v-for="(item, index) in savingItems"
              :key="index"
              class="py-2 text-sm"
            >
              {{ item }}
            </li>
          </ul>
        </div>
        <div>
          <h2 class="text-2xl font-semibold mb-4">대출</h2>
          <ul class="divide-y divide-gray-300">
            <li
              v-for="(item, index) in loanItems"
              :key="index"
              class="py-2 text-sm"
            >
              {{ item }}
            </li>
          </ul>
        </div>
      </div>
  
      <!-- Chart.js 표시부 -->
      <div class="grid grid-cols-3 gap-8 mt-8">
        <div class="bg-gray-200 h-64 flex items-center justify-center">
          <span>chart.js표시부</span>
        </div>
        <div class="bg-gray-200 h-64 flex items-center justify-center">
          <span>chart.js표시부</span>
        </div>
        <div class="bg-gray-200 h-64 flex items-center justify-center">
          <span>chart.js표시부</span>
        </div>
      </div>
  
      <!-- 하단 안내 -->
      <div class="mt-8 text-center text-gray-500 text-sm">
        밑 구분선은 반응형으로 마지막 요소 밑으로
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  // 더미 데이터
  const depositItems = ref([
    'List item 1',
    'List item 2',
    'List item 3',
    'List item 4',
    'List item 5',
    'List item 6',
    'List item 7',
  ]);
  
  const savingItems = ref([
    'List item 1',
    'List item 2',
    'List item 3',
    'List item 4',
    'List item 5',
    'List item 6',
    'List item 7',
  ]);
  
  const loanItems = ref([
    'List item 1',
    'List item 2',
    'List item 3',
    'List item 4',
    'List item 5',
    'List item 6',
    'List item 7',
  ]);
  </script>
  
  <style scoped>
  /* Tailwind CSS를 사용하므로 추가적인 CSS는 필요하지 않음 */
  </style>
  