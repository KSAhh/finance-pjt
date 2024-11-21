<template>
    <div class="container mx-auto px-4 py-8">
      <div>
        <!-- 사용자 정보 섹션 -->
        <div class="grid grid-cols-10 gap-4 border-b pb-4">
          <div class="col-span-6 flex items-center gap-4">
            <ProfileImage
              :image="profileImage"
              @upload="handleProfileImageUpload"
            />
            <div>
              <h2
                class="text-3xl font-bold whitespace-nowrap cursor-pointer hover:underline"
                @click="startEditing"
              >
                {{ nickname }}님의 마이페이지
              </h2>
              <ul class="text-sm text-gray-500 mt-1 whitespace-nowrap">
                <li>답글이 작성되었습니다</li>
                <li>문의내역 답변이 등록</li>
                <li>기타 등등 알림집대성</li>
              </ul>
            </div>
          </div>
          <div class="col-span-2"></div>
          <div class="col-span-2 text-left space-y-2">
            <button @click="goToMyFinancialProduct" class="block hover:underline text-sm">내 금융상품</button>
            <button @click="goToMyComments" class="block hover:underline text-sm">내가 단 댓글</button>
            <button @click="goToMyInquire" class="block hover:underline text-sm">내 문의내역</button>
            <button @click="goToMyInfo" class="block hover:underline text-sm">회원정보수정</button>
          </div>
        </div>
      </div>
  
      <!-- 닉네임 변경 팝업 -->
      <div
        v-if="isEditing"
        class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
      >
        <div class="bg-white rounded-lg p-6 w-96 shadow-lg">
          <h3 class="text-lg font-bold mb-4">닉네임 변경</h3>
          <NickNameChange
            :initialNickname="nickname"
            @update="updateNickname"
            @cancel="cancelEditing"
          />
        </div>
      </div>
  
      <!-- 썸네일 리스트 -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8">
        <div
          v-for="n in 8"
          :key="n"
          class="bg-gray-200 rounded-lg h-32 flex items-center justify-center"
        >
          <span>썸네일</span>
        </div>
      </div>
  
      <div class="mt-8">
        <h3 class="font-bold text-lg mb-2">무슨무슨항목</h3>
        <ul class="divide-y divide-gray-300">
          <li v-for="n in 12" :key="n" class="py-4 flex items-center text-sm">
            <div class="w-8 h-8 bg-indigo-200 rounded-full flex items-center justify-center">
              <span class="text-indigo-600 font-bold">A</span>
            </div>
            <span class="ml-4">List item {{ n }}</span>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import ProfileImage from '@/components/mypage/ProfileImage.vue';
  import NickNameChange from '@/components/mypage/NickNameChange.vue';
  import { useRouter } from 'vue-router';



  const router = useRouter()
  const goToMyComments = () => {
  router.push({ name: 'MyComments' });
};
const goToMyFinancialProduct = () => {
  router.push({ name: "MyFinancialProduct"})
}
const goToMyInquire = () => {
  router.push({ name: "MyInquire"})
}
const goToMyInfo = () => {
  router.push({ name: "MyInfoEdit" })
}
  // 상태 관리
  const profileImage = ref(''); // 프로필 이미지 초기값
  const nickname = ref(''); // 닉네임 초기값
  const isEditing = ref(false); // 닉네임 변경 상태
  
  // 로컬스토리지 키
  const AUTH_KEY_STORAGE = 'key'; // 로그인 시 저장된 인증 키
  const API_URL = 'http://127.0.0.1:8000/accounts/update/'; // 유저 정보 API 엔드포인트
  const API_URL_USER = 'http://127.0.0.1:8000/accounts/user/'; // 유저 정보 API 엔드포인트
  
  // 닉네임 변경 시작
  const startEditing = () => {
    isEditing.value = true;
  };
  
  // 닉네임 변경 취소
  const cancelEditing = () => {
    isEditing.value = false;
  };
  
  // 닉네임 업데이트 (API 요청 포함)
  const updateNickname = async (newNickname) => {
    try {
      const authKey = localStorage.getItem(AUTH_KEY_STORAGE);
  
      if (!authKey) {
        throw new Error('인증 키가 없습니다. 다시 로그인 해주세요.');
      }
  
      // 서버에 PATCH 요청 보내기
      await axios.patch(
        API_URL,
        { nickname: newNickname },
        {
          headers: {
            Authorization: `Token ${authKey}`,
          },
        }
      );
  
      // 상태 업데이트
      nickname.value = newNickname;
      isEditing.value = false;
  
      alert('닉네임이 성공적으로 변경되었습니다.');
    } catch (error) {
      console.error('닉네임 변경 실패:', error.message);
      alert('닉네임 변경에 실패했습니다. 다시 시도해주세요.');
    }
  };
  
  // 프로필 이미지 업로드 (API 요청 포함)
  const handleProfileImageUpload = async (file) => {
    try {
      const authKey = localStorage.getItem(AUTH_KEY_STORAGE);
  
      if (!authKey) {
        throw new Error('인증 키가 없습니다. 다시 로그인 해주세요.');
      }
  
      const reader = new FileReader();
  
      reader.onload = async (event) => {
        const imageBase64 = event.target.result;
  
        // 서버에 PATCH 요청 보내기
        const formData = new FormData();
        formData.append('profile_image', file);
  
        const response = await axios.patch(API_URL, formData, {
          headers: {
            Authorization: `Token ${authKey}`,
            'Content-Type': 'multipart/form-data',
          },
        });
  
        // 프로필 이미지 URL 업데이트
        profileImage.value = response.data.profile_image;
  
        alert('프로필 사진이 성공적으로 변경되었습니다.');
      };
  
      reader.readAsDataURL(file);
    } catch (error) {
      console.error('프로필 사진 업로드 실패:', error.message);
      alert('프로필 사진 업로드에 실패했습니다.');
    }
  };
  
  // 유저 정보 가져오기
  const fetchUserData = async () => {
    try {
      const authKey = localStorage.getItem(AUTH_KEY_STORAGE);
  
      if (!authKey) {
        throw new Error('인증 키가 없습니다. 다시 로그인 해주세요.');
      }
  
      const response = await axios.get(API_URL_USER, {
        headers: {
          Authorization: `Token ${authKey}`,
        },
      });
  
      const userData = response.data;
      nickname.value = userData.nickname || '사용자 별명 없음';
      profileImage.value = userData.profile_image || '';
    } catch (error) {
      console.error('유저 정보 가져오기 실패:', error.message);
      alert('유저 정보를 불러오는데 실패했습니다. 다시 로그인 해주세요.');
    }
  };
  
  // 컴포넌트가 마운트될 때 유저 데이터 가져오기
  onMounted(() => {
    fetchUserData();
  });
  </script>