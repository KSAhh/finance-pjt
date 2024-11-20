<template>
  <li class="px-4 lg:px-6 xl:px-8 relative group">
    <!-- 메뉴 이름 -->
    <a href="#" @click.prevent="onMenuClick" class="hover:underline">
      {{ label }}
    </a>

    <!-- 드롭다운 메뉴 -->
    <div
      v-if="isVisible"
      class="dropdown-menu fixed top-[64px] left-0 w-screen bg-white border border-gray-300 rounded opacity-0 h-0 overflow-hidden transition-all duration-500 ease-in-out group-hover:h-64 group-hover:opacity-100 z-50"
    >
      <div class="flex h-full">
        <!-- 첫 번째 영역 -->
        <div class="w-1/3 bg-gray-100 p-4">
          <h3 class="text-lg font-semibold animate-slide-in-left">{{ label }} 정보</h3>
          <p class="mt-2 text-sm text-gray-600 animate-fade-in">
            {{ label }}에 대한 설명이나 관련 정보가 이 영역에 표시됩니다.
          </p>
        </div>

        <!-- 두 번째 영역 -->
        <div class="w-1/3 bg-white p-4 border-l border-r border-gray-200 animate-fade-in">
          <ul class="space-y-2">
            <li
              v-for="(item, index) in dropdownContent"
              :key="index"
              class="hover:underline cursor-pointer"
              @click="onItemClick(item)"
            >
              {{ item.label || item }}
            </li>
          </ul>
        </div>

        <!-- 세 번째 영역 -->
        <div class="w-1/3 bg-gray-100 p-4 animate-slide-in-right">
          <h3 class="text-lg font-semibold">추가 정보</h3>
          <p class="mt-2 text-sm text-gray-600">
            {{ label }}과 관련된 추가 정보가 표시될 수 있습니다.
          </p>
        </div>
      </div>
    </div>
  </li>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  dropdownContent: {
    type: Array,
    default: () => [],
  },
  isVisible: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(['click-menu', 'click-item']);

function onMenuClick() {
  emit('click-menu', props.label);
}

function onItemClick(item) {
  emit('click-item', item);
}
</script>

<style scoped>
/* 애니메이션 정의 */
@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slide-in-left {
  from {
    transform: translateX(-20px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slide-in-right {
  from {
    transform: translateX(20px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* 애니메이션 클래스 */
.animate-fade-in {
  animation: fade-in 0.5s ease-in-out;
}

.animate-slide-in-left {
  animation: slide-in-left 0.5s ease-in-out;
}

.animate-slide-in-right {
  animation: slide-in-right 0.5s ease-in-out;
}
</style>
