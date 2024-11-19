<template>
    <ul
      class="hidden sm:flex text-base md:text-lg lg:text-xl tracking-wide whitespace-nowrap"
    >
      <MenuItem
        v-for="(item, index) in menuItems"
        :key="index"
        :label="item.label"
        :dropdown-content="item.dropdownContent"
      />
    </ul>
  </template>
  
  <script>
  import MenuItem from "./MenuItem.vue";
  
  export default {
    name: "Menu",
    components: { MenuItem },
    data() {
      return {
        menuItems: [
          { label: "예적금", dropdownContent: ["예적금 상품 1", "예적금 상품 2", "예적금 상품 3"] },
          { label: "대출", dropdownContent: ["대출 상품 1", "대출 상품 2", "대출 상품 3"] },
          { label: "외화예적금", dropdownContent: ["외화예적금 상품 1", "외화예적금 상품 2", "외화예적금 상품 3"] },
          { label: "환율", dropdownContent: ["환율 상품 1", "환율 상품 2", "환율 상품 3"] },
        ],
      };
    },
  };
  </script>
  