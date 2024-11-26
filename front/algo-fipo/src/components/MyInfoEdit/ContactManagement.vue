<template>
  <div class="container mx-auto p-6 bg-white">
    <h1 class="text-2xl font-bold text-gray-900 mb-6">내 정보 수정</h1>
    <form @submit.prevent="updateUserInfo">
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-1" for="nickname">닉네임</label>
        <input
          id="nickname"
          v-model="nickname"
          type="text"
          class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-1" for="profileImage">프로필 이미지</label>
        <div v-if="profileImageUrl" class="mt-2">
          <img :src="profileImageUrl" alt="프로필 이미지" class="w-20 h-20 rounded-full object-cover" />
        </div>
        <input
          id="profileImage"
          type="file"
          @change="onImageChange"
          class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
        />
      </div>
      <button
        type="submit"
        class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md hover:bg-blue-600 transition"
      >
        수정하기
      </button>
    </form>
    <button @click="goToMyInfo"
          type="submit"
          class="bg-blue-500 text-white px-4 py-2 mt-5 rounded-lg shadow-md hover:bg-blue-600 transition"
        >이전으로
      </button>
  </div>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const store = useUserStore()
const router = useRouter()

const nickname = ref('')
const profileImage = ref(null)
const profileImageUrl = ref('') // 기존 프로필 이미지 URL

const onImageChange = (event) => {
  profileImage.value = event.target.files[0];
}

// 페이지 로드 시 기존 유저 정보 설정
onMounted(async () => {
  await store.getUserInfo(); // 유저 정보 가져오기
  const userInfo = store.userInfo;

  nickname.value = userInfo.nickname || ''; // 기존 닉네임 설정
  profileImageUrl.value = userInfo.profile_image || ''; // 기존 프로필 이미지 설정
});

// 회원정보 업데이트 함수
const updateUserInfo = async () => {
  const formData = new FormData();
  if (nickname.value) formData.append('nickname', nickname.value);
  if (profileImage.value) formData.append('profile_image', profileImage.value)

  await store.updateUserInfo(formData)
  alert('회원정보가 수정되었습니다.')
  router.push('/myinfoedit'); // 수정 후 마이페이지 목록으로 이동

};
  const goToMyInfo = () => {
      router.push('/myinfoedit')
    };

</script>

<style scoped>
/* Tailwind CSS 사용 */
</style>
