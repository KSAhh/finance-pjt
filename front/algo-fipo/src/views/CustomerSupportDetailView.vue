<template>
  <div>
    <CSListItemDetail />
    <!-- 댓글 -->
    <CSListItemDetailComment
      :articlePk="articlePk"
      :articleAuthorId="article.author"
      />
    <!-- <h2 class="mt-6">댓글 목록</h2>
    <div v-if="comments && comments.length > 0">
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>댓글작성자: {{ comment.commenter_nickname }}</p>
          <p>내용: {{ comment.comment_body }}</p>
          <button @click="updateComment">댓글 수정</button>
          <button @click="deleteComment">댓글 삭제</button>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>댓글이 없습니다.</p>
    </div> -->
  </div>
</template>

<script setup>
// {
//         "image": null,
//         "is_private": false,
//         "is_delete": false,
//         "created_at": "2024-11-18T07:04:29.255492Z",
//         "updated_at": "2024-11-18T07:04:29.255492Z",
//         "author": 11
//     },

import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useCsStore } from '@/stores/csStore'
import CSListItemDetail from '@/components/CustomerService/CSListItemDetail.vue'
import CSListItemDetailComment from '@/components/CustomerService/CSListItemDetailComment.vue'

const store = useCsStore()
const route = useRoute()
const articlePk = route.params.article_pk;

const comments = computed(() => store.comments[articlePk] || []); // 특정 글의 댓글 데이터 가져오기
const article = computed(() => store.article || {} )
const API_URL = import.meta.env.VITE_API_BASE_URL

onMounted(async () => {
  await store.getComments(articlePk)
})

// 글 수정 함수
const updateArticle = () => {
  const newTitle = prompt('새 제목을 입력하세요:', article.value.title);
  const newContent = prompt('새 내용을 입력하세요:', article.value.article_body);

  if (newTitle && newContent) {
    store.updateArticle(articlePk, { title: newTitle, article_body: newContent });
  }
}

// 글 삭제 함수
const deleteArticle = () => {
  if (confirm('정말로 글을 삭제하시겠습니까?')) {
    store.deleteArticle(articlePk);
  }
}

// 댓글 수정 함수
const updateComment = () => {
  const newContent = prompt('댓글 내용을 수정하세요:');

  if (newContent) {
    store.updateComment(commentId, { comment_body: newContent });
  }
}

// 댓글 삭제 함수
const deleteComment = (commentId) => {
  if (confirm('정말로 댓글을 삭제하시겠습니까?')) {
    store.deleteComment(commentId);
  }
}
</script>

<style scoped>
</style>