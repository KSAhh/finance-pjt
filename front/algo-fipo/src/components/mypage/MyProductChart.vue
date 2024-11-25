<template>
  <div class="chart-container bg-white rounded-lg shadow-md p-4">
    <h2 class="text-xl font-bold mb-4">금리 비교 차트</h2>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>
<script setup>
import { ref, onMounted, watch } from "vue";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

// Props 정의
const props = defineProps({
  depositProducts: Array,
  savingProducts: Array,
  etcProducts: Array,
});

const chartCanvas = ref(null);
let chartInstance = null;

const createChart = () => {
  if (chartInstance) {
    chartInstance.destroy();
  }

  // Labels (상품명 및 기관명)
  const depositLabels = props.depositProducts.map(
    (product) => `${product.kor_co_nm} (${product.fin_prdt_nm})`
  );
  const savingLabels = props.savingProducts.map(
    (product) => `${product.kor_co_nm} (${product.fin_prdt_nm})`
  );
  const etcLabels = props.etcProducts.map(
    (product) => `${product.kor_co_nm} (${product.fin_prdt_nm})`
  );

  // Data
  const depositRates = props.depositProducts.map((product) => product.intr_rate ?? 0);
  const savingRates = props.savingProducts.map((product) => product.intr_rate ?? 0);
  const etcRates = props.etcProducts.map((product) => product.intr_rate ?? 0);

  const labels = [...depositLabels, ...savingLabels, ...etcLabels];
  const datasets = [
    {
      label: "예금 금리 (%)",
      data: [...depositRates, ...Array(savingRates.length + etcRates.length).fill(null)],
      borderColor: "rgba(54, 162, 235, 1)",
      backgroundColor: "rgba(54, 162, 235, 0.2)",
      borderWidth: 2,
      spanGaps: false,
    },
    {
      label: "적금 금리 (%)",
      data: [
        ...Array(depositRates.length).fill(null),
        ...savingRates,
        ...Array(etcRates.length).fill(null),
      ],
      borderColor: "rgba(75, 192, 192, 1)",
      backgroundColor: "rgba(75, 192, 192, 0.2)",
      borderWidth: 2,
      spanGaps: false,
    },
    {
      label: "기타 금리 (%)",
      data: [
        ...Array(depositRates.length + savingRates.length).fill(null),
        ...etcRates,
      ],
      borderColor: "rgba(255, 99, 132, 1)",
      backgroundColor: "rgba(255, 99, 132, 0.2)",
      borderWidth: 2,
      spanGaps: false,
    },
  ];

  chartInstance = new Chart(chartCanvas.value, {
    type: "line",
    data: {
      labels,
      datasets,
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: "금리 비교 (상품 유형별)",
          font: {
            size: 18,
            weight: "bold",
          },
        },
        legend: {
          position: "top",
          labels: {
            font: {
              size: 14,
            },
          },
        },
        tooltip: {
          callbacks: {
            label: (context) => `${context.dataset.label}: ${context.raw ?? "데이터 없음"}%`,
          },
        },
      },
      scales: {
        x: {
          title: {
            display: false,
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
watch(
  [() => props.depositProducts, () => props.savingProducts, () => props.etcProducts],
  createChart,
  { deep: true }
);
</script>

<!-- <script setup>
import { ref, onMounted, watch } from "vue";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

// Props 정의
const props = defineProps({
  depositProducts: Array,
  savingProducts: Array,
  etcProducts: Array,
});

const chartCanvas = ref(null);
let chartInstance = null;

const createChart = () => {
  if (chartInstance) {
    chartInstance.destroy();
  }

  // Labels (상품명 및 기관명)
  const labels = [...props.depositProducts, ...props.savingProducts, ...props.etcProducts].map(
    (product) => `${product.kor_co_nm} (${product.fin_prdt_nm})`
  );

  // Data
  const depositRates = props.depositProducts.map((product) => product.intr_rate || 0);
  const savingRates = props.savingProducts.map((product) => product.intr_rate || 0);
  const etcRates = props.etcProducts.map((product) => product.intr_rate || 0);

  chartInstance = new Chart(chartCanvas.value, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "예금 금리 (%)",
          data: depositRates,
          borderColor: "rgba(54, 162, 235, 1)",
          backgroundColor: "rgba(54, 162, 235, 0.2)",
          borderWidth: 2,
        },
        {
          label: "적금 금리 (%)",
          data: savingRates,
          borderColor: "rgba(75, 192, 192, 1)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderWidth: 2,
        },
        {
          label: "기타 금리 (%)",
          data: etcRates,
          borderColor: "rgba(255, 99, 132, 1)",
          backgroundColor: "rgba(255, 99, 132, 0.2)",
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: "금리 비교 (상품 유형별)",
          font: {
            size: 18,
            weight: "bold",
          },
        },
        legend: {
          position: "top",
          labels: {
            font: {
              size: 14,
            },
          },
        },
        tooltip: {
          callbacks: {
            label: (context) => `${context.dataset.label}: ${context.raw}%`,
          },
        },
      },
      scales: {
        x: {
          title: {
            display: true,
            text: "상품명 (기관명)",
            font: {
              size: 14,
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
watch(
  [() => props.depositProducts, () => props.savingProducts, () => props.etcProducts],
  createChart,
  { deep: true }
);

</script> -->

<style scoped>
.chart-container {
  width: 100%;
  height: auto;
  max-height: 400px;
}
</style>
