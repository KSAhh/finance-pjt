<template>
    <div>
      <h1>글 상세</h1>
      <div v-if="article">
        <p>글 번호: {{ article.id }}</p>
        <p>작성자: {{ article.author_nickname }}</p>
        <p>제목: {{ article.title }}</p>
        <p>내용: {{ article.article_body }}</p>
  
        <!-- 글 작성자만 수정/삭제 버튼 보이도록 설정 -->
        <div v-if="article.author === currentUserId">
          <button @click="updateArticle">글 수정</button>
          <button @click="deleteArticle">글 삭제</button>
        </div>
      </div>
      <div v-else>
        <p>글을 불러오는 중...</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue';
  import axios from 'axios';
  import { useRoute } from 'vue-router';
  import { useUserStore } from '@/stores/user';
  import { useCsStore } from '@/stores/csStore';
  
  const route = useRoute();
  const articlePk = route.params.article_pk;
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
  
  const userStore = useUserStore()
  const currentUserId = computed(() => userStore.userInfo.pk); // 현재 로그인한 사용자 ID
  const store = useCsStore()
  const article = computed(() => store.article || {}); // 글 데이터 가져오기
  
  onMounted(async () => {
    try {
      await store.getArticle(articlePk); // 글 데이터 가져오기 (스토어 함수)
      await userStore.getUserInfo() // 사용자 정보 가져오기
    } catch (error) {
      console.error('글 불러오기 실패:', error);
    }
  });
  
  // 글 수정 함수
  const updateArticle = async () => {
    const newTitle = prompt('새 제목을 입력하세요:', article.value.title);
    const newContent = prompt('새 내용을 입력하세요:', article.value.article_body);
  
    if (newTitle && newContent) {
      try {
        const response = await axios.put(
          `${API_BASE_URL}/api/v1/articles/${articlePk}/`,
          {
            title: newTitle,
            article_body: newContent,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.getItem('key')}`,
            },
          }
        );
        alert('글이 수정되었습니다.');
        await store.getArticle(articlePk); // 수정된 글 데이터 다시 가져오기
      } catch (error) {
        console.error('글 수정 실패:', error);
        alert('글 수정 중 오류가 발생했습니다.');
      }
    }
  };
  
  // 글 삭제 함수
  const deleteArticle = async () => {
    if (confirm('정말로 글을 삭제하시겠습니까?')) {
      try {
        await axios.delete(`${API_BASE_URL}/api/v1/articles/${articlePk}/`, {
          headers: {
            Authorization: `Token ${localStorage.getItem('key')}`,
          },
        });
        alert('글이 삭제되었습니다.');
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
  button {
    margin: 0.5rem;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #f0f0f0;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #e0e0e0;
  }
  </style>
  