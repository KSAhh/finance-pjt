<template>
  <div class="overflow-hidden relative mt-8">
    <div
      ref="carousel"
      class="flex gap-6 transition-transform duration-500"
      :style="{ transform: `translateX(-${currentSlide * slideWidth}px)` }"
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
import { ref, computed, onMounted } from "vue";

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

const currentSlide = ref(0);
const slideWidth = ref(0);

const carousel = ref(null);

onMounted(() => {
  slideWidth.value = carousel.value.offsetWidth;
});

const totalSlides = computed(() => Math.ceil(props.banks.length / 5));

const isSelected = (bank) => props.selectedBanks.includes(bank.id);

const selectBank = (bank) => {
  emit("select-bank", bank);
};

const prevSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value--;
  }
};

const nextSlide = () => {
  if (currentSlide.value < totalSlides.value - 1) {
    currentSlide.value++;
  }
};
</script>

<style scoped>
/* 추가적인 스타일이 필요한 경우 여기에 작성하세요 */
</style>
