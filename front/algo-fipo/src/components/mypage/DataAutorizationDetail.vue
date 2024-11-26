<template>
  <div class="container mx-auto p-6 bg-white">
    <h1 class="text-2xl font-bold text-gray-900 mb-6">유저 정보</h1>
    <div v-if="isLoading">
      <p class="text-lg text-gray-600">데이터를 불러오는 중입니다...</p>
    </div>
    <form v-else @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label for="gender" class="block text-gray-700 font-bold mb-2">성별</label>
        <select
          id="gender"
          v-model="userData.gender"
          class="border rounded w-full py-2 px-3"
          required
        >
          <option value="">선택하세요</option>
          <option value="남">남</option>
          <option value="여">여</option>
        </select>
      </div>

      <div class="mb-4">
        <label for="birth_date" class="block text-gray-700 font-bold mb-2">출생일</label>
        <input
          id="birth_date"
          type="date"
          v-model="userData.birth_date"
          class="border rounded w-full py-2 px-3"
          required
          :max="today"
        />
      </div>
 
          <div class="mb-4">
        <label for="monthly_income" class="block text-gray-700 font-bold mb-2">월 소득</label>
        <input
          id="monthly_income"
          type="number"
          v-model="userData.monthly_income"
          class="border rounded w-full py-2 px-3"
          min="0"
          required
          @keypress="validateNumber"
        />
      </div>

      <div class="mb-4">
        <label for="monthly_expense" class="block text-gray-700 font-bold mb-2">월 소비</label>
        <input
          id="monthly_expense"
          type="number"
          v-model="userData.monthly_expense"
          class="border rounded w-full py-2 px-3"
          min="0"
          required
          @keypress="validateNumber"
        />
      </div>

      <div class="mb-4">
        <label for="total_assets" class="block text-gray-700 font-bold mb-2">총 자산</label>
        <input
          id="total_assets"
          type="number"
          v-model="userData.total_assets"
          class="border rounded w-full py-2 px-3"
          min="0"
          required
          @keypress="validateNumber"
        />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700">마이데이터 동의</label>
        <input
          v-model="userData.is_mydata_consent"
          type="checkbox"
          class="mt-2"
        />
      </div>

      <button
        type="submit"
        class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md hover:bg-blue-600 transition"
      >
        {{ isDataFetched ? "정보수정" : "정보생성" }}
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
import { ref, computed, onMounted } from "vue"
import { useRouter } from 'vue-router';
import axios from "axios"

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL
const today = new Date().toISOString().split("T")[0];
const isDataFetched = ref(false);
const isLoading = ref(true)
const router = useRouter()

const userData = ref({
  gender: "",
  birth_date: "",
  monthly_income: 0,
  monthly_expense: 0,
  total_assets: 0,
  is_mydata_consent: false,
})

onMounted(async () => {
  await fetchUserData()
  isLoading.value = false
})



// 숫자 입력만 허용
const validateNumber = (event) => {
  const charCode = event.charCode || event.keyCode;
  if (charCode < 48 || charCode > 57) {
    event.preventDefault();
  }
}


// 유저 정보 조회
const fetchUserData = async () => {
  const token = localStorage.getItem('key')

  try {
    const response = await axios.get(`${API_BASE_URL}/accounts/assets/`, {
      headers: {Authorization:`Token ${token}`}
    });
    userData.value = response.data;
    isDataFetched.value = true
    console.log("정보 조회 성공:", userData.value);
  } catch (error) {
    if (error.response && error.response.status === 404) {
    } else {
      console.error("정보 조회 실패:", error);
    }
  }
}

const handleSubmit = async () => {
  try {
    const url = `${API_BASE_URL}/accounts/assets/`;
    const method = isDataFetched.value ? "put" : "post"; // PUT for 수정, POST for 생성
    const response = await axios[method](url, userData.value, {
      headers: {
        Authorization: `Token ${localStorage.getItem("key")?.trim()}`,
      },
    });

    isDataFetched.value = true;
    alert("성공적으로 저장되었습니다.");
    console.log("응답 데이터:", response.data);
  } catch (error) {
    console.error("요청 실패:", error.response || error);
    alert("요청 중 문제가 발생했습니다.");
  }
}


const goToMyInfo = () => {
    router.push('/myinfoedit')
  };
</script>

<style scoped>
/* Tailwind CSS 사용 */
</style>

