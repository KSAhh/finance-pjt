import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useUserStore = defineStore('user', () => {
  const users = ref([])
  const userInfo = ref([])
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL 

  // 유저 정보 조회
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

  // 유저 정보 수정
  const updateUserInfo = async (formData) => {
    const token = localStorage.getItem('key');
    await axios
      .patch(`${API_BASE_URL}/accounts/update/`, formData, {
        headers: { Authorization: `Token ${token}` },
      })
      .then((res) => {
        console.log('회원정보 수정 성공:', res.data);
        userInfo.value = res.data;
      })
      .catch((err) => console.error('회원정보 수정 실패:', err));
  };

  return { users, userInfo, getUserInfo, updateUserInfo }
})
