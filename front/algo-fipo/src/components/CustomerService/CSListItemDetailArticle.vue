<template>
  <div class="bg-white rounded-lg shadow p-6">
      <div v-if="article">
        <h2 class="text-xl font-semibold text-gray-800 mb-4">{{ article.title }}</h2>
        <p class="text-gray-700 mb-4">{{ article.article_body }}</p>
        <div v-if="article.image" class="mb-6">
          <img
          :src="formattedImageUrl(article.image)"
          alt="글 이미지"
          class="w-full h-auto rounded-lg shadow-md article-image"
          />
        </div>
        <div class="mb-6">
          <p class="text-sm text-gray-500">글 번호: {{ article.id }}</p>
          <p class="text-sm text-gray-500">작성자: {{ article.author_nickname }}</p>
        </div>
        <div class="flex justify-end space-x-4">
          <!-- 글 작성자만 수정/삭제 버튼 보이도록 설정 -->
          <div v-if="article.author === currentUserId" class="flex space-x-4">
            <button
              @click="updateArticle"
              class="px-4 py-2 rounded-md shadow"
            >
              글 수정
            </button>
            <button
              @click="deleteArticle"
              class="px-4 py-2 rounded-md shadow"
            >
              글 삭제
            </button>
          </div>
        </div>
      </div>
      <div v-else class="text-center text-gray-500">
        <p>글을 불러오는 중...</p>
      </div>
    </div>
</template>
  
<script setup>
  import { ref, computed, onMounted } from 'vue'
  import axios from 'axios'
  import { useRoute, useRouter } from 'vue-router'
  import { useUserStore } from '@/stores/user'
  import { useCsStore } from '@/stores/csStore'
  
  const route = useRoute()
  const router = useRouter()
  const articlePk = route.params.article_pk
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
  
  const userStore = useUserStore()
  const currentUserId = computed(() => userStore.userInfo.pk); // 현재 로그인한 사용자 ID
  const store = useCsStore()
  const article = computed(() => store.article || {}); // 글 데이터 가져오기
  
  onMounted(async () => {
    try {
      await store.getArticle(articlePk); // 글 데이터 가져오기 (스토어 함수)
      await userStore.getUserInfo() // 사용자 정보 가져오기
      console.log(store.article)
    } catch (error) {
      console.error('글 불러오기 실패:', error);
    }
  })
  
  const formattedImageUrl = (imagePath) => {
    if (!imagePath) return null; // 이미지가 없으면 null 반환
    return imagePath.startsWith('http') ? imagePath : `${API_BASE_URL}${imagePath}`;
  }

  // 글 수정 함수
  const updateArticle = () => {
    router.push({ name: 'CustomerSupportEditView', params: { article_pk: articlePk } });
  }

  
  // 글 삭제 함수
  const deleteArticle = async () => {
    if (confirm('정말로 글을 삭제하시겠습니까?')) {
      try {
        await axios.delete(`${API_BASE_URL}/api/v1/articles/${articlePk}/`, {
          headers: {
            Authorization: `Token ${localStorage.getItem('key')}`,
          },
        });
        // 삭제 후 다른 페이지로 이동 (예: 메인 페이지)
        window.location.href = '/';
      } catch (error) {
        console.error('글 삭제 실패:', error);
        alert('글 삭제 중 오류가 발생했습니다.');
      }
    }
  };
</script>
  
<style scoped>
/* 버튼 디자인 개선 */
button {
  margin: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
}

/* 이미지 스타일 */
.article-image {
  margin-bottom: 1.5rem;
  width: 100%;
  max-width: 600px;
  height: auto;
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

button {
  margin: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #fff; /* 기본 배경 흰색 */
  color: #000; /* 기본 텍스트 검은색 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 기본 쉐도우 */
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; /* 부드러운 전환 효과 */
}

button:hover {
  background-color: #000; /* 호버 시 배경 검은색 */
  color: #fff; /* 호버 시 텍스트 흰색 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 호버 시 쉐도우 더 강조 */
}

</style>