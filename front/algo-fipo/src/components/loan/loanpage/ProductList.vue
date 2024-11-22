<!-- src/components/loan/loanpage/ProductList.vue -->
<template>
    <div class="product-list">
      <!-- 상품 목록 렌더링 로직 -->
      <div v-for="product in filteredProducts" :key="product.id" class="product-item">
        <h3>{{ product.name }}</h3>
        <p>{{ product.description }}</p>
        <!-- ... 기타 상품 정보 ... -->
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  import { financialCompanies } from '@/components/loan/loanpage/filterOptions.js';
  
  // Props 정의
  const props = defineProps({
    filters: {
      type: Object,
      default: () => ({}),
    },
  });
  
  // 예시 상품 데이터 (실제 데이터는 API 호출 등을 통해 받아올 수 있음)
  const products = [
    { id: 1, name: '상품 A', description: '설명 A', financialCompany: 'BNK경남은행' },
    { id: 2, name: '상품 B', description: '설명 B', financialCompany: 'KB국민은행' },
    // ... 기타 상품 ...
  ];
  
  // 필터링 로직
  const filteredProducts = computed(() => {
    return products.filter((product) => {
      // 금융사 필터 적용
      if (props.filters.financialCompanies && props.filters.financialCompanies.length > 0) {
        return props.filters.financialCompanies.includes(product.financialCompany);
      }
      // 추가적인 필터링 로직을 원할 경우 여기에 추가
      return true;
    });
  });
  </script>
  
  <style scoped>
  .product-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  
  .product-item {
    border: 1px solid #ddd;
    padding: 20px;
    border-radius: 8px;
  }
  </style>
  