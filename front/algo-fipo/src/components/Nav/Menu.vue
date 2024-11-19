<template>
  <ul
    class="hidden sm:flex text-base md:text-lg lg:text-xl tracking-wide whitespace-nowrap"
  >
  <MenuItem
  v-for="(item, index) in menuItems"
  :key="index"
  :label="item.label"
  :dropdownContent="item.dropdownContent"
/>

  </ul>
</template>

<script setup>
import { reactive } from "vue";
import MenuItem from "./MenuItem.vue";

// 메뉴 항목 정의
const menuItems = reactive([
  {
    label: "예적금",
    dropdownContent: ["예적금 상품 1", "예적금 상품 2", "예적금 상품 3"],
  },
  {
    label: "대출",
    dropdownContent: ["대출 상품 1", "대출 상품 2", "대출 상품 3"],
  },
  {
    label: "외화예적금",
    dropdownContent: [
      "외화예적금 상품 1",
      "외화예적금 상품 2",
      "외화예적금 상품 3",
    ],
  },
  {
    label: "환율",
    dropdownContent: ["환율 상품 1", "환율 상품 2", "환율 상품 3"],
  },
]);
</script>

<style scoped>
/* 필요 시 스타일 추가 */
</style>
