import { defineStore } from "pinia";

export const useNavBarStore = defineStore("navBar", {
  state: () => ({
    isLoggedIn: !!localStorage.getItem("key"),
    userFullName: localStorage.getItem("fullname") || "",
  }),
  actions: {
    login(fullName) {
      this.isLoggedIn = true;
      this.userFullName = fullName;
    },
    logout() {
      this.isLoggedIn = false;
      this.userFullName = "";
      localStorage.removeItem("key");
      localStorage.removeItem("fullname");
    },
  },
});
