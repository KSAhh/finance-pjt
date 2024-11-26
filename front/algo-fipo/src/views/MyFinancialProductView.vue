<template>
    <div class="container mx-auto px-4 py-8">
      <!-- 제목 -->
      <h1 class="text-4xl font-bold mb-8">내 금융상품</h1>
      
      <!-- 금융상품 리스트 -->
      <div class="grid grid-cols-3 gap-8 border-b pb-6">
          <!-- 예금 -->
          <MyProductList
            title="예금"
            :products="depositProducts"
          />

          <!-- 적금 -->
          <MyProductList
            title="적금"
            :products="savingProducts"
          />

          <!-- 기타 -->
          <MyProductList
            title="기타"
            :products="etcProducts"
          />
      </div>
  
      <!-- Chart.js 표시부 -->
      <div class="grid grid-cols-3 gap-8 mt-8">
      <MyProductChart
        :products="depositProducts"
        chartTitle="예금 금리 비교"
      />
      <MyProductChart
        :products="savingProducts"
        chartTitle="적금 금리 비교"
      />
      <MyProductChart
        :products="etcProducts"
        chartTitle="기타 상품 금리 비교"
      />
    </div>



    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue';
  import { useProductStore } from '@/stores/productStore'
  import MyProductList from '@/components/mypage/MyProductList.vue';
  import MyProductChart from '@/components/mypage/MyProductChart.vue';

  const store = useProductStore()
  
  // 페이지 로드 시 데이터 가져오기
  onMounted(async () => {
    await store.getUserProducts()
  });
  // 통화 형식으로 변환 함수
  // const formatCurrency = (value) => {
  //   return new Intl.NumberFormat("ko-KR", {
  //     style: "currency",
  //     currency: "KRW",
  //   }).format(value);
  // };

const depositProducts = computed (() => store.userProducts.deposits)
const savingProducts = computed (() => store.userProducts.savings)
const etcProducts = computed (() => store.userProducts.etc)
// 모든 상품을 하나의 배열로 합치기 (차트용)
// const allProductsForChart = computed(() => [
//   ...store.userProducts.deposits,
//   ...store.userProducts.savings,
//   ...store.userProducts.etc,
// ])

</script>

<style scoped>
/* Tailwind CSS를 사용하므로 추가적인 CSS는 필요하지 않음 */
</style>
  