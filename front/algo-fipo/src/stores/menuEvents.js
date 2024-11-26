import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useMenuEventsStore = defineStore('menuEvents', () => {
  const selectedMenu = ref(null); // 대분류 메뉴 선택
  const selectedDropdownItem = ref(null); // 드롭다운 메뉴 항목 선택

  const selectMenu = (menu) => {
    selectedMenu.value = menu;
  
    // 대분류 메뉴에 따라 기본값 설정
    if (menu === "예적금") {
      selectedDropdownItem.value = "예금"; // 기본값 설정
    } else if (menu === "대출") {
      selectedDropdownItem.value = "대출"; // 기본값 설정
    } else {
      selectedDropdownItem.value = null; // 다른 메뉴일 경우 초기화
    }
  };
  

  // 드롭다운 메뉴 항목 선택
  const selectDropdownItem = (item) => {
    selectedDropdownItem.value = item;
  };

  return {
    selectedMenu,
    selectedDropdownItem,
    selectMenu,
    selectDropdownItem,
  };
});
