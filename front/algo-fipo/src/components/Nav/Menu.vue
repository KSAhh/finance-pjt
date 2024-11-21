<template>
  <ul class="hidden sm:flex text-base md:text-lg lg:text-xl tracking-wide whitespace-nowrap relative">
    <MenuItem
      v-for="(item, index) in menuItems"
      :key="index"
      :label="item.label"
      :dropdownContent="item.dropdownContent"
      :isVisible="currentOpenDropdown === index"
      @click-item="handleItemClick"
      @click-menu="navigateToMainPage"
      @mouseenter="openDropdown(index)"
      @mouseleave="closeDropdown"
    />
  </ul>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import MenuItem from "./MenuItem.vue";

const router = useRouter();
const currentOpenDropdown = ref(null);

// 메뉴 항목 정의 (보험 메뉴 제거)
const menuItems = reactive([
  {
    label: "예적금",
    dropdownContent: [
      { label: "예금 추천", category: "예금" },
      { label: "적금 추천", category: "적금" },
    ],
  },
  {
    label: "대출",
    dropdownContent: ["대출 알아보기"],
  },
  {
    label: "연금저축",
    dropdownContent: ["상품 1", "상품 2", "상품 3"],
  },
  {
    label: "환율",
    dropdownContent: ["환율 상품 1", "환율 상품 2", "환율 상품 3"],
  },
]);

// 드롭다운 열기
const openDropdown = (index) => {
  currentOpenDropdown.value = index;
};

// 드롭다운 닫기
const closeDropdown = () => {
  currentOpenDropdown.value = null;
};

// 드롭다운 아이템 클릭 이벤트
const handleItemClick = (item) => {
  const selectedItem = menuItems[currentOpenDropdown.value];
  if (selectedItem.label === "대출") {
    router.push({ name: "LoanPage" });
  } else if (selectedItem.label === "예적금") {
    const category = selectedItem.dropdownContent.find(
      (content) => content.label === item.label
    )?.category;
    router.push({ name: "SavingsPage", query: { category } });
  }
  closeDropdown(); // 드롭다운 닫기
};

// 대분류 클릭 이벤트
const navigateToMainPage = (label) => {
  if (label === "대출") {
    router.push({ name: "LoanPage" });
  } else if (label === "예적금") {
    router.push({ name: "SavingsPage", query: { category: "예금" } });
  }
};
</script>


<style scoped>
ul > li::before {
  content: "";
  position: absolute;
  inset: -12px -8px; /* 위아래로 12px, 좌우로 8px 확장 */
  z-index: -1;
  background-color: transparent; /* 시각적 변경 없음 */
}
</style>
