<template>
  <div class="overflow-hidden relative">
    <div
      ref="carousel"
      class="flex gap-4 transition-transform duration-500"
      :style="{ transform: `translateX(-${currentSlide * slideWidth}px)` }"
    >
      <div
        v-for="bank in banks"
        :key="bank.id"
        class="min-w-[150px] p-4 rounded-lg shadow cursor-pointer"
        @click="toggleBankSelection(bank)"
        :class="[
          isSelected(bank) ? 'bg-blue-100' : 'bg-gray-200',
        ]"
      >
        <img :src="bank.logo || '/default-logo.png'" alt="Bank Logo" class="w-16 h-16 mx-auto mb-2" />
        <p class="text-center">{{ bank.name }}</p>
      </div>
    </div>
    <!-- 화살표 버튼 -->
    <button
      class="absolute top-1/2 left-0 -translate-y-1/2 bg-gray-300 p-2 rounded-full"
      @click="prevSlide"
    >
      &lt;
    </button>
    <button
      class="absolute top-1/2 right-0 -translate-y-1/2 bg-gray-300 p-2 rounded-full"
      @click="nextSlide"
    >
      &gt;
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";

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

const emit = defineEmits(["select-bank"]);

const carousel = ref(null);
const currentSlide = ref(0);
const slideWidth = 150;

// 선택된 은행인지 확인
const isSelected = (bank) => props.selectedBanks.includes(bank.id);

// 은행 선택 상태 토글
const toggleBankSelection = (bank) => {
  emit("select-bank", bank);
};

const prevSlide = () => {
  currentSlide.value = Math.max(currentSlide.value - 1, 0);
};

const nextSlide = () => {
  const totalSlides = props.banks.length - Math.floor(carousel.value.offsetWidth / slideWidth);
  currentSlide.value = Math.min(currentSlide.value + 1, totalSlides);
};
</script>

<style scoped>
/* 필요 시 스타일 추가 */
</style>
