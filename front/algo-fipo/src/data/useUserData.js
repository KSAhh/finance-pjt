import { ref } from 'vue';
import axios from 'axios';

export default function useUserData() {
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
  const token = localStorage.getItem('key'); // 저장된 토큰 가져오기

  const userData = ref({});
  const profileImage = ref('');

  // Axios 공통 설정
  const axiosInstance = axios.create({
    baseURL: API_BASE_URL,
    headers: {
      Authorization: `Token ${token}`,
    },
  });

  // 사용자 정보 가져오기
  const fetchUserData = async () => {
    if (!token) {
      console.error('Token not found');
      throw new Error('로그인 토큰이 없습니다.');
    }

    try {
      const { data } = await axiosInstance.get('/accounts/user/');
      userData.value = data;
      profileImage.value = data.profile_image; // 프로필 이미지만 업데이트
    } catch (error) {
      console.error('사용자 정보를 불러오는 데 실패했습니다.', error);
      throw error;
    }
  };

  const updateProfileImage = async (file) => {
    if (!token) {
      console.error('Token not found');
      throw new Error('로그인 토큰이 없습니다.');
    }
  
    const formData = new FormData();
    formData.append('profile_image', file);
  
    try {
      const { data } = await axiosInstance.patch('/accounts/update/', formData);
      profileImage.value = data.profile_image; // 상태 업데이트
      return data.profile_image; // 새로운 프로필 이미지 URL 반환
    } catch (error) {
      console.error('프로필 사진 업데이트 실패', error);
      throw error;
    }
  };
  
  const updateNicknameOnServer = async (newNickname) => {
    if (!token) {
      throw new Error('로그인 토큰이 없습니다.');
    }
  
    try {
      const response = await axios.patch(
        '/accounts/update/',
        { nickname: newNickname },
        {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error('닉네임 업데이트 실패:', error);
      throw error;
    }
  };
  

  

  return {
    userData,
    profileImage,
    fetchUserData,
    updateProfileImage,
    updateNicknameOnServer,
  };
}
