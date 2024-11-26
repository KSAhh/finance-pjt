<template>
    <div class="container mx-auto p-6 bg-white">
      <div class="content">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">회원정보수정</h1>
        <ul class="divide-y divide-gray-300 border-t border-gray-300">
          <li v-for="(item, index) in menuItems" :key="index" class="py-2 text-sm text-gray-700">
            <router-link
              :to="item.route"
              class="text-sm text-gray-700 hover:underline"
            >
              {{ item.label }}
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  // 메뉴 항목 정의
  const menuItems = ref([
    { label: "내 정보 수정", route: "/myinfoedit/contact-management" },
    { label: "비밀번호 수정", route: "/myinfoedit/password-edit" },
    { label: "내 금융정보 수정", route: "/myinfoedit/finance-info-edit" },
    { label: "마이데이터 권한", route: "/myinfoedit/data-authorization" },
    { label: "알림", route: "/myinfoedit/notifications" },
    { label: "회원 탈퇴", route: "/myinfoedit/account-deletion" },
  ]);
  </script>
  
  <style scoped>
  /* Tailwind CSS 사용으로 추가 스타일링 필요하지 않음 */
  </style>
  