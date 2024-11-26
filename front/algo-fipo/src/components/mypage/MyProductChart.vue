<template>
  <div class="chart-container bg-white rounded-lg shadow-md p-4">
    <h2 class="text-xl font-bold mb-4">{{ chartTitle }}</h2>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

// Props 정의
const props = defineProps({
  products: Array, // 상품 데이터 배열
  chartTitle: String, // 차트 제목
});

const chartCanvas = ref(null);
let chartInstance = null;

const createChart = () => {
  if (chartInstance) {
    chartInstance.destroy();
  }

  // Labels (상품명)
  const labels = props.products.map(
    (product) => `${product.fin_prdt_nm}`
  );
 
  // Data
  const rates = props.products.map((product) => product.intr_rate ?? 0);

  chartInstance = new Chart(chartCanvas.value, {
    type: "bar",
    data: {
      labels,
      datasets: [
        {
          label: "금리 (%)",
          data: rates,
          borderColor: "rgba(75, 192, 192, 1)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: props.chartTitle,
          font: {
            size: 18,
            weight: "bold",
          },
        },
        legend: {
          display: false,
        },
        tooltip: {
          callbacks: {
            label: (context) =>
              `${context.dataset.label}: ${context.raw}%`,
          },
        },
      },
      scales: {
        x: {
          title: {
            display: true,
            text: "상품명",
            font: {
              size: 14,
            },
          },
          ticks: {
            callback: function (value, index) {
              const label = labels[index]
              if (label ) {
                return label.split(" "); // 공백 기준으로 배열 반환 (줄바꿈 처리)
              }
              return ""; // 라벨이 없으면 빈 문자열
            },
        },
        },
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: "금리 (%)",
            font: {
              size: 14,
            },
          },
          ticks: {
            callback: (value) => `${value}%`,
          },
        },
      },
    },
  });
};

// 차트 생성 또는 업데이트
onMounted(createChart);
watch(() => props.products, createChart, { deep: true });
</script>

<style scoped>
.chart-container {
  width: 100%;
  max-height: 400px;
}
</style>
