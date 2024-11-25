<template>
    <li class="py-4 flex flex-col border rounded-lg shadow-sm px-4 bg-white">
      <p><strong>상품명:</strong> {{ product.fin_prdt_nm }}</p>
      <p><strong>기관명:</strong> {{ product.kor_co_nm }}</p>
      <p><strong>가입 기간:</strong> {{ product.duration_months }}개월</p>
      <p><strong>예치 금액:</strong> {{ formatCurrency(product.balance) }}</p>
      <p><strong>가입일:</strong> {{ product.start_date }}</p>
      <p><strong>만기일:</strong> {{ product.end_date }}</p>
    </li>
  </template>
  
  <script setup>
  defineProps({
    product : Object,
  })
      const formatCurrency = (value) => {
        return new Intl.NumberFormat("ko-KR", {
          style: "currency",
          currency: "KRW",
        }).format(value);
      };

    //   {
        // 미사용데이터
    //     "id": 1,
    //     "product_type": "예금",
    //     "duration_months": 36,
    //     "user": 11,
    //     "deposit_product": 107,
    //     "saving_product": null
    // }
  </script>
  
  <style scoped>
  /* Tailwind CSS 사용 */
  </style>
  