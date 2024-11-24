import { defineStore } from "pinia";

export const useFilterStore = defineStore("filterStore", {
  state: () => ({
    selectedBanks: [],
    selectedPreferences: [],
    filters: {
      durations: [], // 기본적으로 빈 배열
      types: [], // 기본적으로 빈 배열
    },
    selectedCategory: "예금", // 기본 카테고리
  }),
  actions: {
    resetFilters() {
      this.selectedBanks = [];
      this.selectedPreferences = [];
      this.filters = {
        durations: [],
        types: [],
      };
    },
  },
});
