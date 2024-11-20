<!-- <template>
    <div class="flex justify-center items-center border-b pb-4">
      <div class="space-x-4">
        <button
          v-for="category in categories"
          :key="category"
          @click="$emit('select-category', category)"
          class="py-2 px-4 rounded-lg"
          :class="category === selectedCategory ? 'bg-blue-600 text-white' : 'bg-gray-100 text-black'"
        >
          {{ category }}
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    categories: Array,
    selectedCategory: String,
  });
  </script>
  
  <style scoped>
  /* 스타일 필요 시 작성 */
  </style>
   -->