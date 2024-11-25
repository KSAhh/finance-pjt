// 변경
import { ref } from 'vue'
import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductStore = defineStore("productStore", () => {
  const products = ref({
    deposits: [],
    savings: [],
  })
  const isLoading = ref(false)
  const error = ref(null)
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

  // 상품 전체데이터 가져오기
  const fetchProducts = async () => {
    isLoading.value = true
    error.value = null

    await axios.get(`${API_BASE_URL}/api/v1/products/`)
    .then((res) => {
      products.value = {
        deposits: res.data.deposits || [],
        savings: res.data.savings || [],
      }
    })
    .catch((err) => {
      console.log("API 요청 중 오류 발생:", err)
    })
    .finally(() => {
      isLoading.value = false
    })
  }
  return { products, isLoading, error, fetchProducts}
})

// 기존
// import { defineStore } from "pinia";
// import axios from "axios";

// const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

// export const useProductStore = defineStore("productStore", {
//     state: () => ({
//       products: {
//         deposits: [],
//         savings: [],
//       },
//       isLoading: false,
//       error: null,
//     }),
  
//     actions: {
//       async fetchProducts() {
//         this.isLoading = true;
//         this.error = null;
  
//         try {
//           const response = await axios.get(`${API_BASE_URL}/api/v1/products/`);
//           this.products = {
//             deposits: response.data.deposits || [],
//             savings: response.data.savings || [],
//           };
//         } catch (err) {
//           console.error("API 요청 중 오류 발생:", err.message);
//           this.error = err.message;
//         } finally {
//           this.isLoading = false;
//         }
//       },
//     },
//   });