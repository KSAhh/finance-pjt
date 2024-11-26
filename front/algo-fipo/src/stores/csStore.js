// store/csStore.js
import { ref } from 'vue'
import { defineStore } from "pinia";
import axios from 'axios'

export const useCsStore = defineStore("cs", () => {
  const articles = ref([])
  const comments = ref({})
  const article = ref([])

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
  const getComments = (async (articlePk) => {
    await axios.get(`${API_URL}/api/v1/articles/${articlePk}/`)
    .then(res => {
      console.log(res.data)
      article.value = res.data.article
      comments.value[articlePk] = res.data.comments
      console.log(article)
      console.log(comments.value)
    })
    .catch(err => console.log(err))
  })

  // 글 생성하기
  const createArticle = (async (articleData) => {
    const token = localStorage.getItem('key')

    const formData = new FormData();
    formData.append('title', articleData.title);
    formData.append('article_body', articleData.article_body);
    if (articleData.image) formData.append('image', articleData.image); // 이미지 추가
    formData.append('is_private', articleData.is_private || false); // 기본값 false

    console.log("토큰", token)
    await axios.post(`${API_URL}/api/v1/articles/`, formData,
    {
      headers: {
        Authorization: `Token ${token}`,
        'Content-Type': 'multipart/form-data',
      },
    })
    .then((res) => {
      console.log('글 작성 성공:');
      console.log(res)
    })
    .catch((err) => console.log("글 작성 실패", err))
  })
  return { articles, comments, getArticles, getComments, article, createArticle }
}, { persist: true})
