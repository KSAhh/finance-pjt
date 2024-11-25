<template>
  <!-- <div class="p-6 max-w-4xl mx-auto bg-white rounded-lg shadow-lg"> -->
    <h2 class="text-2xl font-bold mb-6">기준 환율 차트
      <p class="text-sm text-gray-500 mb-6">{{ store.exchanges[0]?.updated_at }} 기준</p>
    </h2>
    
    <canvas ref="chartCanvas"></canvas>
  <!-- </div> -->
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import { useExchangeStore } from "@/stores/exchangeStore";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const store = useExchangeStore();
const chartCanvas = ref(null); // 차트를 렌더링할 캔버스
let chartInstance = null // Chart.js 인스턴스


// 차트 생성 함수
const createChart = () => {
  if (chartInstance) {
    chartInstance.destroy(); // 기존 차트 제거
  }

  // 데이터 준비
  const labels = store.exchanges.map((exchange) => exchange.cur_nm);
  const data = store.exchanges.map((exchange) => exchange.cur_to_krw);

  chartInstance = new Chart(chartCanvas.value, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "기준 환율 [KRW]",
          data,
          backgroundColor: "rgba(54, 162, 235, 0.2)",
          borderColor: "#1C6CE6",
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true, // 반응형 크기
      plugins: {
        legend: { // 범례
          display: true,
          position: "top",
        },
      },
      scales: {
        x: {
          title: {
            display: true,
            text: "통화 코드",
          },
        },
        y: {
          title: {
            display: true,
            text: "기준 환율 (KRW)",
          },
          ticks: {
            callback: (value) => value.toLocaleString(),
          },
        },
      },
    },
  });
};

// 데이터 가져오기 및 차트 생성
onMounted(async () => {
  if (store.exchanges.length === 0) {
    await store.getExchangeRate(); // 데이터가 없는 경우 가져오기
  }
  createChart(); // 차트 생성
});

// 컴포넌트가 해제될 때 차트 제거
onBeforeUnmount(() => {
  if (chartInstance) {
    chartInstance.destroy();
    chartInstance = null;
  }
});
</script>

<style scoped>
canvas {
  width: 100%;
  height: 400px;
}
</style>
