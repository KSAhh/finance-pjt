import { defineStore } from "pinia";
import { banks, savingsBanks } from "@/data/bankData";

export const useBankNameStore = defineStore("bankNameStore", {
  state: () => ({
    banks, // 일반 은행 데이터
    savingsBanks, // 저축은행 데이터
  }),

  getters: {
    // 모든 은행 데이터를 합쳐서 반환
    allBanks(state) {
      return [...state.banks, ...state.savingsBanks];
    },

    // 특정 은행 이름으로 검색
    getBankByName: (state) => (name) => {
      return state.allBanks.find((bank) => bank.name === name) || null;
    },
  },

  actions: {
    // 은행 추가
    addBank(bank) {
      this.banks.push(bank);
    },

    // 저축은행 추가
    addSavingsBank(bank) {
      this.savingsBanks.push(bank);
    },

    // 은행 제거
    removeBank(id) {
      this.banks = this.banks.filter((bank) => bank.id !== id);
    },

    // 저축은행 제거
    removeSavingsBank(id) {
      this.savingsBanks = this.savingsBanks.filter((bank) => bank.id !== id);
    },
  },
});
