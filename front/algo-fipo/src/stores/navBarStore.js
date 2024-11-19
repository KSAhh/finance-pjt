// store/navBarStore.js
import { defineStore } from "pinia";

export const useNavBarStore = defineStore("navBar", {
  state: () => ({
    isLoggedIn: !!localStorage.getItem("key"),
    userFullName: localStorage.getItem("fullname") || "",
  }),
  actions: {
    logout() {
      this.isLoggedIn = false;
      this.userFullName = "";
    },
    login(fullName) {
      this.isLoggedIn = true;
      this.userFullName = fullName;
    },
  },
});
