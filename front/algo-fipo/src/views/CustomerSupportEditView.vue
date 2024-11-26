<template>
    <div class="min-h-screen bg-gray-50 flex justify-center items-center p-6">
      <div class="max-w-3xl w-full bg-white rounded-lg shadow-lg p-8">
        <h1 class="text-2xl font-bold text-gray-800 mb-6">글 수정</h1>
        <form @submit.prevent="submitEdit">
          <!-- 제목 입력 -->
          <div class="mb-4">
            <label for="title" class="block text-sm font-medium text-gray-700 mb-1">제목</label>
            <input
              id="title"
              v-model="title"
              type="text"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="수정할 제목을 입력하세요"
              required
            />
          </div>
          <!-- 본문 입력 -->
          <div class="mb-4">
            <label for="body" class="block text-sm font-medium text-gray-700 mb-1">내용</label>
            <textarea
              id="body"
              v-model="body"
              rows="6"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="수정할 내용을 입력하세요"
              required
            ></textarea>
          </div>
          <!-- 이미지 업로드 -->
          <div class="mb-4">
            <label for="image" class="block text-sm font-medium text-gray-700 mb-1">이미지</label>
            <input
              id="image"
              type="file"
              accept="image/*"
              @change="handleImageUpload"
              class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div>
          <!-- 비공개 설정 -->
          <div class="mb-4">
            <label for="isPrivate" class="block text-sm font-medium text-gray-700 mb-1">비공개 설정</label>
            <input
              id="isPrivate"
              type="checkbox"
              v-model="isPrivate"
              class="mr-2"
            />
            <span class="text-sm text-gray-600">비공개로 설정하려면 체크하세요</span>
          </div>
          <!-- 수정 버튼 -->
          <div class="flex justify-end">
            <button
              type="submit"
              class="px-4 py-2 text-white bg-blue-500 rounded-lg shadow-md hover:bg-blue-600 transition"
            >
              수정 완료
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import { useCsStore } from '@/stores/csStore';
  
  const router = useRouter();
  const route = useRoute();
  const store = useCsStore();
  
  const articlePk = route.params.article_pk;
  const title = ref('');
  const body = ref('');
  const isPrivate = ref(false); // 비공개 여부
  const imageFile = ref(null); // 업로드된 이미지 파일
  
  // 이미지 파일 핸들링
  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      imageFile.value = file;
    }
  };
  
  // 기존 데이터 가져오기
  onMounted(async () => {
    try {
      await store.getArticle(articlePk);
      const article = store.article;
  
      // 기존 데이터 바인딩
      title.value = article.title;
      body.value = article.article_body;
      isPrivate.value = article.is_private;
    } catch (error) {
      console.error('글 데이터 불러오기 실패:', error);
    }
  });
  
  // 수정 제출
  const submitEdit = async () => {
    store.updateArticle(articlePk, {
      title: title.value,
      article_body: body.value,
      is_private: isPrivate.value,
      image: imageFile.value, // 업로드된 이미지 추가
    })
    // Vue Router를 사용해 리다이렉트
    console.log("articlepk", articlePk)
    router.push({ name: "CustomerSupportDetail", params: {article_pk: articlePk} });

}

  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
  }
  button {
    padding: 0.5rem 1rem;
    border-radius: 4px;
  }
  input[type='file'] {
    display: block;
    margin-top: 0.5rem;
  }
  </style>
  