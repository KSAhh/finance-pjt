// store/exchangeStore.js
import { ref } from 'vue'
import { defineStore } from "pinia";
import axios from 'axios'

export const useExchangeStore = defineStore("exchangeStore", () => {
  const exchanges = ref([])
  const API_URL = "http://127.0.0.1:8000"

  // 데이터 다운로드
  const getExchangeRate = (async () => {
    await axios.get(`${API_URL}/api/v1/exchange/`)
    .then(res => {
      exchanges.value = res.data
    })
    .catch(err => console.log(err))
  })

  return { exchanges, getExchangeRate }
})
