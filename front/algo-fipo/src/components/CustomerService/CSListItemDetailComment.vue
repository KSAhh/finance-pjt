<template>
<div class="bg-white rounded-lg shadow p-6">
      <h2 class="text-2xl font-bold text-gray-800 mb-6">댓글 목록</h2>
      <div v-if="comments && comments.length > 0" class="space-y-6">
        <ul>
          <li v-for="comment in comments" :key="comment.id" class="p-4 border-b border-gray-200">
            <p class="text-sm text-gray-500">작성자: <span class="font-semibold">{{ comment.commenter_nickname }}</span></p>
            <!-- 수정 중인지 확인 -->
            <div v-if="editingCommentId === comment.id" class="mt-4">
              <textarea 
                v-model="editingCommentBody"
                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              ></textarea>
              <div class="flex justify-end space-x-4 mt-2">
                <button 
                  @click="saveEditComment(comment.id)" 
                  class="bg-blue-500 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-600 transition"
                >
                  저장
                </button>
                <button 
                  @click="cancelEdit" 
                  class="bg-gray-300 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 transition"
                >
                  취소
                </button>
              </div>
            </div>

            <div v-else>
              <p class="text-gray-700 mt-2">{{ comment.comment_body }}</p>

              <!-- 현재 사용자와 작성자 비교 -->
              <div v-if="comment.commenter === currentUserId" class="flex justify-end space-x-4 mt-2">
                <button 
                  @click="startEditComment(comment.id, comment.comment_body)" 
                  class="px-4 py-2 rounded-md shadow-md hover:bg-yellow-600 transition"
                >
                  댓글 수정
                </button>
                <button 
                  @click="deleteComment(comment.id)" 
                  class="px-4 py-2 rounded-md shadow-md hover:bg-red-600 transition"
                >
                  댓글 삭제
                </button>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div v-else>
        <p class="text-gray-500">댓글이 없습니다.</p>
      </div>
      <div class="comment-form mt-8">
        <h3 class="text-lg font-semibold text-gray-800 mb-4">댓글 작성</h3>
        <textarea
          v-model="newCommentBody"
          placeholder="댓글을 입력하세요"
          class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        ></textarea>
        <div class="flex justify-end mt-2">
          <button 
            @click="addComment"
            class="px-4 py-2 rounded-md "
          >
            댓글 추가
          </button>
        </div>
      </div>
    </div>
</template>
  
<script setup>
  import { ref, computed, onMounted } from 'vue'
  import { useCsStore } from '@/stores/csStore'
  import axios from 'axios';
  import { useUserStore } from '@/stores/user'
  
   
  const props = defineProps({
    articlePk: Number,
  })

  const userStore = useUserStore()
  const currentUserId = computed( () => userStore.userInfo.pk)
  const token = localStorage.getItem('key') // 로컬스토리지에서 토큰 가져오기

  const store = useCsStore()
  const newCommentBody = ref('')
  const editingCommentId = ref(null) // 수정 중인 댓글 ID
  const editingCommentBody = ref('') // 수정 중인 댓글 내용

  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL
  const comments = computed(() => store.comments[props.articlePk] || []) // 특정 글의 댓글 데이터 가져오기
  
  onMounted(async () => {
      await userStore.getUserInfo()
      await store.getArticle(props.articlePk) // 댓글 데이터 가져오기
  })
  
  // 댓글 추가
  const addComment = async () => {
    if (!newCommentBody.value.trim()) {
      alert('댓글 내용을 입력하세요.')
      return
    }
    const newComment = {
      comment_body: newCommentBody.value,
      is_delete: false, // 기본값 설정
    }
    try {
      const response = await axios.post(
        `${API_BASE_URL}/api/v1/articles/${props.articlePk}/comment/`,
        newComment,
        {
          headers: {
            Authorization: `Token ${token}`, // Token 키로 토큰 추가
          },
        }
      )
      // 댓글 추가 성공 시, 스토어 업데이트
      await store.getArticle(props.articlePk) // 댓글 목록 갱신
      newCommentBody.value = '' // 입력 필드 초기화
    } catch (error) {
      console.error(error)
      alert(error.response.data ,'댓글 추가에 실패했습니다.')
    }
  }
    
  // 댓글 수정 시작
  const startEditComment = (commentId, commentBody) => {
    editingCommentId.value = commentId
    editingCommentBody.value = commentBody
  }
  // 댓글 수정 저장
  const saveEditComment = async (commentId) => {
    if (!editingCommentBody.value.trim()) {
      alert('수정 내용을 입력하세요.')
      return
    }
    try {
      const response = await axios.put(
        `${API_BASE_URL}/api/v1/articles/comment/${commentId}/`,
        {
          comment_body: editingCommentBody.value,
          is_delete: false,
        },
        {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
      )
      // 성공적으로 수정된 경우 스토어 업데이트
      await store.getArticle(props.articlePk)

      editingCommentId.value = null
      editingCommentBody.value = ''
    } catch (error) {
      console.error('댓글 수정 실패:', error)
      alert(error.response.data.detail, '댓글 수정에 실패했습니다.')
    }
  }
  // 댓글 삭제 함수
  const deleteComment = async (commentId) => {
    if (confirm('정말로 댓글을 삭제하시겠습니까?')) {
      try {
        const token = localStorage.getItem('key'); // 로컬스토리지에서 토큰 가져오기

        const response = await axios.delete(
          `${import.meta.env.VITE_API_BASE_URL}/api/v1/articles/comment/${commentId}/`,
          {
            headers: {
              Authorization: `Token ${token}`,
            },
          }
        );
        // 댓글 삭제 후 목록 갱신 (스토어나 상태 업데이트)
        await store.getArticle(props.articlePk);
      } catch (error) {
        console.error('댓글 삭제 실패:', error);
      }
    }
  };
</script>
  
<style scoped>
/* 전체 레이아웃 */
.bg-gray-50 {
  min-height: 100vh;
  padding: 2rem;
}

textarea {
  resize: none;
}

button {
  margin: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
}

button {
  font-size: 0.875rem;

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