<template>
    <div class="top-rates">
      <h1>금융상품 추천 [마이데이터 미동의]</h1>
  
      <!-- 로딩 상태 -->
      <div v-if="isLoading" class="loading">
        <span>🔄 데이터를 불러오는 중...</span>
      </div>
  
      <!-- 에러 상태 -->
      <div v-else-if="error" class="error">
        ❌ {{ error }}
      </div>
  
      <!-- 데이터 표시 -->
      <div v-else>
        <h2>예금 상품 (Top 10)</h2>
        <ul v-if="depositTopRates.length > 0" class="card-list">
          <li v-for="(item, index) in depositTopRates" :key="index" class="card">
            <h3>{{ item.product.name }}</h3>
            <p>금융사: <strong>{{ item.product.company }}</strong></p>
            <p>금리 유형: <strong>{{ item.intr_rate_type_nm }}</strong></p>
            <p>저축 기간: <strong>{{ item.save_trm }}개월</strong></p>
            <p>최고 금리: <strong>{{ item.intr_rate2 }}%</strong></p>
          </li>
        </ul>
        <p v-else class="empty-data">예금 상품 데이터가 없습니다.</p>
  
        <h2>적금 상품 (Top 10)</h2>
        <ul v-if="savingTopRates.length > 0" class="card-list">
          <li v-for="(item, index) in savingTopRates" :key="index" class="card">
            <h3>{{ item.product.name }}</h3>
            <p>금융사: <strong>{{ item.product.company }}</strong></p>
            <p>금리 유형: <strong>{{ item.intr_rate_type_nm }}</strong></p>
            <p>저축 기간: <strong>{{ item.save_trm }}개월</strong></p>
            <p>최고 금리: <strong>{{ item.intr_rate2 }}%</strong></p>
          </li>
        </ul>
        <p v-else class="empty-data">적금 상품 데이터가 없습니다.</p>
      </div>
    </div>
  </template>
  
  
  
  <script setup>
  import { onMounted, computed } from "vue";
  import { useProductStore } from "@/stores/productStore";
  
  const productStore = useProductStore();
  
  // 데이터 Fetch
  onMounted(() => {
    productStore.fetchTopRates();
  });
  
  // 상태 및 데이터 계산
  const depositTopRates = computed(() => productStore.topRates.deposits);
  const savingTopRates = computed(() => productStore.topRates.savings);
  const isLoading = computed(() => productStore.isLoading);
  const error = computed(() => productStore.error);
  </script>
  
  <style scoped>
  /* 기본 컨테이너 스타일 */
  .top-rates {
    font-family: Arial, sans-serif;
    margin: 20px auto;
    max-width: 800px;
    text-align: center;
  }
  
  /* 로딩 상태 스타일 */
  .loading {
    color: #007bff;
    font-size: 18px;
    background: #f0f8ff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  /* 에러 상태 스타일 */
  .error {
    color: #ff4d4f;
    font-size: 16px;
    background: #fff5f5;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  /* 제목 스타일 */
  h1 {
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
  }
  
  h2 {
    margin-top: 20px;
    font-size: 20px;
    color: #007bff;
  }
  
  /* 카드 리스트 스타일 */
  .card-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin: 20px 0;
    padding: 0;
    list-style: none;
  }
  
  /* 카드 스타일 */
  .card {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: left;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
  }
  
  .card h3 {
    margin: 0 0 8px;
    font-size: 18px;
    color: #333;
  }
  
  .card p {
    margin: 4px 0;
    font-size: 14px;
    color: #555;
  }
  
  .card strong {
    color: #0f4681;
  }
  
  /* 빈 데이터 스타일 */
  .empty-data {
    font-size: 16px;
    color: #888;
    margin: 20px 0;
  }
  </style>
  