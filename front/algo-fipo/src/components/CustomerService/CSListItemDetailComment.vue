<template>
  <div>
    <h2 class="mt-6">댓글 목록</h2>
    <div v-if="comments && comments.length > 0">
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>댓글작성자: {{ comment.commenter_nickname }}</p>

          <!-- 수정 중인지 확인 -->
          <div v-if="editingCommentId === comment.id">
            <textarea v-model="editingCommentBody"></textarea>
            <button @click="saveEditComment(comment.id)">저장</button>
            <button @click="cancelEdit">취소</button>
          </div>

          <div v-else>
            <p>내용: {{ comment.comment_body }}</p>

            <!-- 현재 사용자와 작성자 비교 -->
            <div v-if="comment.commenter === currentUserId">
              <button @click="startEditComment(comment.id, comment.comment_body)">댓글 수정</button>
              <button @click="deleteComment(comment.id)">댓글 삭제</button>
            </div>
          </div>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>댓글이 없습니다.</p>
    </div>
    <div class="comment-form">
      <h3>댓글 작성</h3>
      <textarea v-model="newCommentBody" placeholder="댓글을 입력하세요"></textarea>
      <button @click="addComment">댓글 추가</button>
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
      await store.getComments(props.articlePk) // 댓글 데이터 가져오기
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
      await store.getComments(props.articlePk) // 댓글 목록 갱신
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
      await store.getComments(props.articlePk)

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
        await store.getComments(props.articlePk);
      } catch (error) {
        console.error('댓글 삭제 실패:', error);
      }
    }
  };
</script>
  
<style scoped>
  .comment-form {
    margin-top: 1rem;
  }
  textarea {
    width: 100%;
    height: 4rem;
    margin-bottom: 0.5rem;
  }
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
  