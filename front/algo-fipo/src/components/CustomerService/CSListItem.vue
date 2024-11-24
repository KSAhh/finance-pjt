<template>
  <h5>글번호: {{ article.id }}</h5>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.article_body }}</p>
    <img v-if="article.image" :src="article.image" alt="첨부이미지">
    <p>작성일 : {{ article.created_at }}</p>
    <p>작성자 : {{ article.author }}</p>

    <!-- 댓글 출력 -->
    <!-- <div v-if="comments.length > 0">
      <h3>댓글</h3>
      <ul>
        <li v-for="(comment, index) in comments" :key="index">
          {{ comment.content }}
        </li>
      </ul>
    </div>
    <p v-else>댓글이 없습니다.</p> -->
</template>

<script setup>
defineProps({
  article: Object,
  comments: Array,
})
</script>

<style scoped>

</style>