<template>
  <div
    ref="carouselContainer"
    class="overflow-hidden relative mt-8"
    @wheel.prevent="onWheel"
  >
    <div
      ref="carousel"
      class="flex gap-6 transition-transform duration-300"
      :style="{ transform: `translateX(-${scrollPosition}px)` }"
    >
      <div
        v-for="bank in banks"
        :key="bank.id"
        class="min-w-[150px] p-4 rounded-lg shadow cursor-pointer flex flex-col items-center justify-center transition duration-300"
        @click="selectBank(bank)"
        :class="[
          isSelected(bank) ? 'bg-blue-100 border-2 border-blue-600' : 'bg-gray-100 hover:bg-gray-200',
        ]"
      >
        <img :src="bank.logo || '/default-logo.png'" alt="Bank Logo" class="w-16 h-16 mb-2" />
        <p class="text-center font-medium">{{ bank.name }}</p>
      </div>
    </div>
    <!-- 화살표 버튼 -->
    <button
      class="absolute top-1/2 left-0 -translate-y-1/2 bg-white text-gray-700 p-2 rounded-full shadow-md hover:bg-gray-100 transition duration-300"
      @click="prevSlide"
    >
      &lt;
    </button>
    <button
      class="absolute top-1/2 right-0 -translate-y-1/2 bg-white text-gray-700 p-2 rounded-full shadow-md hover:bg-gray-100 transition duration-300"
      @click="nextSlide"
    >
      &gt;
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';

const props = defineProps({
  banks: {
    type: Array,
    required: true,
  },
  selectedBanks: {
    type: Array,
    required: true,
  },
});

const emit = defineEmits(['select-bank']);

const carouselContainer = ref(null);
const carousel = ref(null);

const scrollPosition = ref(0);

const isSelected = (bank) => props.selectedBanks.includes(bank.id);

const selectBank = (bank) => {
  emit('select-bank', bank);
};

const scrollStep = 150; // Pixels to scroll per wheel event or arrow button click

const updateScrollPosition = () => {
  // Ensure scrollPosition is within valid range
  const maxScroll = carousel.value.scrollWidth - carouselContainer.value.clientWidth;
  if (scrollPosition.value < 0) {
    scrollPosition.value = 0;
  } else if (scrollPosition.value > maxScroll) {
    scrollPosition.value = maxScroll;
  }
};

const onWheel = (event) => {
  const delta = event.deltaY;
  if (delta > 0) {
    // Scroll right
    scrollPosition.value += scrollStep;
  } else {
    // Scroll left
    scrollPosition.value -= scrollStep;
  }
  updateScrollPosition();
};

const prevSlide = () => {
  scrollPosition.value -= carouselContainer.value.clientWidth;
  updateScrollPosition();
};

const nextSlide = () => {
  scrollPosition.value += carouselContainer.value.clientWidth;
  updateScrollPosition();
};

onMounted(() => {
  scrollPosition.value = 0;
});
</script>

<style scoped>
/* Add any additional styles if needed */
</style>
