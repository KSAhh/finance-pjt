<template>
  <div class="bg-gray-50 min-h-screen">
    <div class="max-w-5xl mx-auto bg-white rounded-lg shadow-lg p-8 mt-10">
      <!-- 환율 계산기 -->
      <ExchangeCal />
    </div>

    <div class="max-w-5xl mx-auto bg-white rounded-lg shadow-lg p-8 mt-10">
      <!-- 전체 환율 리스트 -->
      <ExchangeChart />
    </div>
  </div>
</template>

<script setup>
import ExchangeChart from '@/components/ExchangeRate/ExchangeChart.vue'
import ExchangeCal from '@/components/ExchangeRate/ExchangeCal.vue'

</script>

<style scoped>

</style>