// store/csStore.js
import { ref } from 'vue'
import { defineStore } from "pinia";
import axios from 'axios'

export const useCsStore = defineStore("cs", () => {
  const articles = ref([])
  const comments = ref([])
  const token = ref(null)
  const API_URL = "http://127.0.0.1:8000"

  // 데이터 다운로드
  const getArticles = (async () => {
    await axios.get(`${API_URL}/api/v1/articles/`)
    .then(res => {
      console.log(res)
      articles.value = res.data
      // articles.value = res.data.map(article => {
      //   if (article.image) {
      //     article.image = `${API_URL}${article.image}`;
      //   }
      //   return article;
      // })
      console.log(articles.value)
    })
    .catch(err => console.log(err))
  })

  return { articles, comments, getArticles }
}, { persist: true})
