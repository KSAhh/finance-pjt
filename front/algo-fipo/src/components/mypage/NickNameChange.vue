<template>
  <div class="flex flex-col items-center">
    <input
      v-model="editedNickname"
      class="border-b-2 border-gray-300 focus:outline-none focus:border-blue-500 px-2 py-1 w-full"
      type="text"
      placeholder="새 닉네임을 입력하세요"
    />
    <div class="flex justify-end mt-2 w-full">
      <button
        @click="cancelChange"
        class="px-4 py-1 mr-2 bg-gray-300 rounded hover:bg-gray-400"
      >
        취소
      </button>
      <button
        @click="confirmChange"
        class="px-4 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        확인
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

// Props and Emits
const props = defineProps({
  initialNickname: {
    type: String,
    default: '', // Default value to prevent undefined issues
  },
});

const emit = defineEmits(['update', 'cancel']);

// Initialize editedNickname from props
const editedNickname = ref(props.initialNickname);

// Watch for changes in props.initialNickname
watch(
  () => props.initialNickname,
  (newValue) => {
    editedNickname.value = newValue || ''; // Update editedNickname if props change
  },
  { immediate: true }
);

// Confirm nickname change
const confirmChange = () => {
  if (!editedNickname.value.trim()) {
    alert('닉네임은 비어 있을 수 없습니다.');
    return;
  }
  emit('update', editedNickname.value.trim()); // Emit updated nickname
};

// Cancel nickname change
const cancelChange = () => {
  emit('cancel');
};
</script>

