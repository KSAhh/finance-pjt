<template>
  <div class="chart-container bg-white rounded-lg shadow-md p-4">
    <h2 class="text-xl font-bold mb-4">금리 비교 차트</h2>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

// Props 정의
const props = defineProps({
  products: Array
})

// 차트 캔버스 참조
const chartCanvas = ref(null) // 차트를 렌더링할 캔버스
let chartInstance = null  // Chart.js 인스턴스

const createChart = () => {
  if (chartInstance) {
    chartInstance.destroy();
  }

  const labels = props.products.map(
    (product) => `${product.kor_co_nm} (${product.fin_prdt_nm})`
  );
  const data = props.products.map((product) => product.intr_rate);

  chartInstance = new Chart(chartCanvas.value, {
    type: 'bar',
    data: {
      labels,
      datasets: [
        {
          label: '금리 (%)',
          data,
          backgroundColor: 'rgba(54, 162, 235, 0.6)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true, // 반응형 크기
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: '금리 (%)',
          },
        },
        x: {
          title: {
            display: true,
            text: '상품명 (기관명)',
          },
        },
      },
      plugins: { 
        legend: {
          display: false,
        },
      },
    },
  });
};

// 차트 생성 또는 업데이트
onMounted(createChart)
watch(() => props.products, createChart, { deep: true });

</script>

<style scoped>
.chart-container {
  width: 100%;
  height: auto;
  max-height: 400px;
}
</style>
