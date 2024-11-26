<template>
  <li class="p-6 flex flex-col border rounded-lg shadow-lg bg-white hover:shadow-xl transition">
    <div class="mb-4">
      <h3 class="text-lg font-bold text-gray-800 mb-2">{{ product.fin_prdt_nm }}</h3>
      <p class="text-sm text-gray-500">{{ product.kor_co_nm }}</p>
    </div>
    <div class="grid grid-cols-2 gap-4">
      <div>
        <p class="text-sm font-semibold text-gray-700">가입 기간</p>
        <p class="text-sm text-gray-600">{{ product.duration_months }}개월</p>
      </div>
      <div>
        <p class="text-sm font-semibold text-gray-700">예치 금액</p>
        <p class="text-sm text-gray-600">{{ formatCurrency(product.balance) }}</p>
      </div>
      <div>
        <p class="text-sm font-semibold text-gray-700">금리</p>
        <p class="text-sm text-gray-600">{{ product.intr_rate }}%</p>
      </div>
      <div>
        <p class="text-sm font-semibold text-gray-700">가입일</p>
        <p class="text-sm text-gray-600">{{ product.start_date }}</p>
      </div>
      <div>
        <p class="text-sm font-semibold text-gray-700">만기일</p>
        <p class="text-sm text-gray-600">{{ product.end_date }}</p>
      </div>
    </div>
  </li>
</template>

<script setup>
defineProps({
  product: Object,
});

const formatCurrency = (value) => {
  return new Intl.NumberFormat("ko-KR", {
    style: "currency",
    currency: "KRW",
  }).format(value);
};
</script>

<style scoped>
/* Tailwind CSS 사용 */
</style>
