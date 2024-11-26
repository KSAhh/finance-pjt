
import { defineStore } from "pinia";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const useProductStore = defineStore("productStore", {
    state: () => ({
      products: {
        deposits: [],
        savings: [],
      },
      isLoading: false,
      error: null,
    }),
  
    actions: {
      async fetchProducts() {
        this.isLoading = true;
        this.error = null;
  
        try {
          const response = await axios.get(`${API_BASE_URL}/api/v1/products/`);
          this.products = {
            deposits: response.data.deposits || [],
            savings: response.data.savings || [],
          };
        } catch (err) {
          console.error("API 요청 중 오류 발생:", err.message);
          this.error = err.message;
        } finally {
          this.isLoading = false;
        }
      },
    },
  });