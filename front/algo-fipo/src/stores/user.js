import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useUserStore = defineStore('user', () => {
  const users = ref([])
  const userInfo = ref([])
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL 

  const getUserInfo = async () => {
    const token = localStorage.getItem('key')
    await axios.get(`${API_BASE_URL}/accounts/user/`, {
      headers : { Authorization : `Token ${token}`}
    })
    .then( (res) => {
      userInfo.value = res.data
      console.log("사용자 정보 조회", userInfo.value)
      return res.data
    })
    .catch( (err) => console.log(err))
  }

  return { users, userInfo, getUserInfo }
})
