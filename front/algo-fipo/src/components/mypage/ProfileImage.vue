<template>
  <div
    class="relative w-24 h-24 bg-gray-200 rounded-full flex items-center justify-center overflow-hidden cursor-pointer group"
    @click="triggerFileInput"
  >
    <img
      v-if="image"
      :src="image"
      alt="프로필 사진"
      class="absolute inset-0 w-full h-full object-cover"
    />
    <span v-else class="text-gray-700 text-sm">사진 업로드</span>
    <div
      class="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity"
    >
      <span class="text-white text-xs">사진 변경</span>
    </div>
    <input
      type="file"
      accept="image/*"
      ref="fileInput"
      class="hidden"
      @change="handleFileChange"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Props
defineProps({
  image: {
    type: String,
    default: '',
  },
});

// Emits
const emit = defineEmits(['upload']);

// 상태
const fileInput = ref(null);

// 파일 입력창 열기
const triggerFileInput = () => {
  fileInput.value.click();
};

// 파일 변경 처리
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    const fileUrl = URL.createObjectURL(file); // 미리보기용 URL 생성
    emit('upload', file); // 부모 컴포넌트로 파일 전달
  }
};
</script>

<style scoped>
/* 필요 시 추가 스타일 */
</style>
