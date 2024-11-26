// 변경
import { ref } from 'vue'
import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductStore = defineStore("productStore", () => {
  
  // 전체상품
  const products = ref({
    deposits: [],
    savings: [],
  })

  // 유저 가입상품
  const userProducts = ref({
    deposits: [],
    savings: [],
    etc: [],
  })

  // Top-rate 상품
  const topRates = ref({
    deposits: [],
    savings: [],
  });


  const isLoading = ref(false)
  const error = ref(null)
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

  // 상품 전체데이터 가져오기
  const fetchProducts = async () => {
    isLoading.value = true
    error.value = null

    await axios.get(`${API_BASE_URL}/api/v1/products/`)
    .then((res) => {
      console.log("응답값1 - res.data.deposits.options있음", res.data)

      // products.value = {
      //   deposits: res.data.deposits || [],
      //   savings: res.data.savings || [],
      // }
      products.value = {
        deposits: (res.data.deposits || []).map((deposit) => ({
          ...deposit,
          options: Array.isArray(deposit.options) ? deposit.options : [], // options가 배열이 아닐 경우 빈 배열로 초기화
        })),
        savings: (res.data.savings || []).map((saving) => ({
          ...saving,
          options: Array.isArray(saving.options) ? saving.options : [], // options가 배열이 아닐 경우 빈 배열로 초기화
        })),
      };
      
      console.log("저장된 값", products.value.deposits[0])
      console.log("응답값2 - res.data.deposits.options없음", res.data)
    })
    .catch((err) => {
      console.log("API 요청 중 오류 발생:", err)
    })
    .finally(() => {
      console.log("먼저 로딩 상태")
      isLoading.value = false
    })
  }

  // 유저가 가입한 상품데이터 가져오기
  const getUserProducts = async () => {
    const token = localStorage.getItem("key")
    if (!token) {
      console.error("토큰이 존재하지 않습니다.")
      return
    }

    await axios.get(`${API_BASE_URL}/api/v1/products/user/`, {
      headers: { Authorization: `Token ${token}`}
    })
    .then((res) => {
      const deposits = []
      const savings = []
      const etc = []

      res.data.forEach((product) => {
          if (product.product_type === "예금") {
            deposits.push(product)
          } else if (product.product_type === "적금") {
            savings.push(product)
          } else {
            etc.push(product)
          }
      });
      userProducts.value = { deposits, savings, etc, }
      console.log("store에 저장된 유저 가입 상품 데이터:", userProducts.value);
    })
    .catch((err) => console.log(err))
  }

    // Top-rate 데이터 가져오기
  const fetchTopRates = async () => {
    isLoading.value = true;
    error.value = null;

    try {
      const response = await axios.get(`${API_BASE_URL}/api/v1/products/top-rate/`);
      topRates.value = {
        deposits: response.data.deposit_top_rates || [],
        savings: response.data.saving_top_rates || [],
      };
    } catch (err) {
      error.value = err.response ? err.response.data.message : "네트워크 오류";
    } finally {
      isLoading.value = false;
    }
  };


  return { products, isLoading, error, fetchProducts, userProducts, getUserProducts, fetchTopRates, topRates}
})
