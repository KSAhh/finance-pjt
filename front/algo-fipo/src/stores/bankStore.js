
// store/bankStore.js
import { defineStore } from "pinia";
import { banks, savingsBanks } from "@/data/bankData";

export const useBankStore = defineStore("bankStore", {
  state: () => ({
    banks,
    savingsBanks,
  }),
});
