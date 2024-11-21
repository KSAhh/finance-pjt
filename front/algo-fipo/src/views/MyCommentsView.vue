<template>
    <div class="container mx-auto p-6 bg-white">
      <div class="content">
        <h1 class="text-4xl font-bold text-gray-900 mb-6">작성 댓글 목록</h1>
        <ul
          class="comment-list border-t border-gray-300 divide-y divide-gray-300"
          v-if="comments.length > 0"
        >
          <li
            v-for="(item, index) in comments"
            :key="index"
            class="comment-item px-4 py-3 text- text-gray-700"
          >
            {{ item }}
          </li>
        </ul>
        <div
          v-else
          class="no-comments text-center text-base text-gray-500 font-medium mt-10"
        >
        작성한 댓글이 없습니다
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const comments = ref([
    // "List item 1",
    // "List item 2",
    // "List item 3",
    // "List item 4",
    // "List item 5",
  ]); // 예제 데이터
  </script>
  
  <style scoped>
  /* Tailwind CSS 사용으로 추가 스타일링 불필요 */
  </style>
  