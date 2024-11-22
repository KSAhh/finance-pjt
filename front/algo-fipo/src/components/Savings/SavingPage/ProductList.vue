<template>
  <div>
    <h2 class="text-xl font-semibold mb-4">상품 리스트</h2>
    <!-- 로딩 상태 -->
    <div v-if="isLoading">
      <p>상품 데이터를 불러오는 중입니다...</p>
    </div>
    <!-- 상품 데이터 -->
    <div v-else-if="products && products.length > 0">
      <div
        v-for="product in products"
        :key="product.id"
        class="product-card"
      >
        <h4 class="font-medium">{{ product.fin_prdt_nm }}</h4>
        <p class="text-sm text-gray-600">{{ product.kor_co_nm }}</p>
        <p>{{ formattedJoinWay(product.join_way) }}</p>
      </div>
    </div>
    <!-- 데이터 없음 -->
    <p v-else>조회된 상품이 없습니다.</p>
  </div>
</template>

<script setup>
defineProps({
  products: {
    type: Array,
    required: true,
  },
  isLoading: {
    type: Boolean,
    required: true,
  },
});

const formattedJoinWay = (joinWay) => {
  if (!joinWay) return "정보 없음";
  if (Array.isArray(joinWay)) {
    return joinWay.join(", ");
  }
  try {
    const parsed = JSON.parse(joinWay.replace(/'/g, '"'));
    return Array.isArray(parsed) ? parsed.join(", ") : parsed;
  } catch (e) {
    console.error("join_way 파싱 실패:", joinWay, e);
    return joinWay;
  }
};
</script>

<style scoped>
.product-card {
  border: 1px solid #ddd;
  padding: 16px;
  margin-bottom: 12px;
  border-radius: 8px;
  background-color: #f9f9f9;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.product-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
