<template>
  <ul class="hidden sm:flex text-base md:text-lg lg:text-xl tracking-wide whitespace-nowrap">
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
    label: "은행 지도",
    dropdownContent: ["주변 은행 찾기"],
  },
  {
    label: "환율",
    dropdownContent: ["환율 조회"],
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
  } else if (selectedItem.label === "은행 지도") {
    const category = selectedItem.dropdownContent.find(
      (content) => content.label === item.label
    )?.category;
    router.push({ name: "BankMap", query: { category } });
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
    else if (label === "은행 지도") {
    router.push({ name: "BankMap"});
  }
    else if (label === "환율") {
    router.push({ name: "ExchangeView" })
  }
};
</script>


<style scoped>

/* ul > li::before {
  content: "";
  position: absolute;
  inset: -12px -8px;
  z-index: -1;
  background-color: transparent;
}
ul > li {
  position: relative;
  overflow: hidden; 
  font-weight: bold;
}

ul > li::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background-color: #0048e8;
  transition: all 0.3s ease; 
  transform: translateX(-50%);
}

ul > li:hover::after {
  width: 80%; 
}

ul > li {
  padding: 0 10px;
  cursor: pointer;
  transition: color 0.3s ease;
} */

ul > li::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
}

ul > li {
  position: relative;
  padding: 12px 16px;
  cursor: pointer;
  transition: color 0.3s ease;
  display: flex;
  align-items: center;
  font-weight: bold;
}

ul > li::after {
  content: "";
  position: absolute;
  bottom: 11px;
  left: 50%;
  width: 0;
  height: 2px;
  background-color: #0048e8;
  transition: width 0.3s ease; /* left는 고정, width만 애니메이션 적용 */
  transform: translateX(-50%);
}

ul > li:hover::after {
  width: 70%; /* 호버 시 밑줄 확장 */
}


</style>
