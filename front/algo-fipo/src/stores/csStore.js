// store/csStore.js
import { ref } from 'vue'
import { defineStore } from "pinia";
import axios from 'axios'

export const useCsStore = defineStore("cs", () => {
  const articles = ref([])
  const comments = ref({})
  const token = ref(null)
  const API_URL = "http://127.0.0.1:8000"

  // 글 데이터 가져오기
  const getArticles = (async () => {
    await axios.get(`${API_URL}/api/v1/articles/`)
    .then(res => {
      articles.value = res.data
    })
    .catch(err => console.log(err))
  })

  // 댓글 데이터 가져오기
  const getComments = (async (article_pk) => {
    await axios.get(`${API_URL}/api/v1/articles/${article_pk}/`)
    .then(res => {
      console.log(res.data)
      comments.value[article_pk] = res.data.comments
      console.log(comments.value)
    })
    .catch(err => console.log(err))
  })

  return { articles, comments, getArticles, getComments }
}, { persist: true})
