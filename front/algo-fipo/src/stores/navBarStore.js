import { defineStore } from "pinia";

export const useNavBarStore = defineStore("navBar", {
  state: () => ({
    isLoggedIn: !!localStorage.getItem("key"),
    // userFullName: localStorage.getItem("fullname") || "",
    userNickname: localStorage.getItem("nickname") || "",
  }),
  actions: {
    login(nickname) {
      this.isLoggedIn = true;
      // this.userNickname = nickname;
    },
    // login(fullName) {
    //   this.isLoggedIn = true;
    //   this.userFullName = fullName;
    // },
    logout() {
      this.isLoggedIn = false;
      // this.userFullName = "";
      this.userNiname = "";
      localStorage.removeItem("key");
      // localStorage.removeItem("fullname");
      localStorage.removeItem("nickname");
    },
  },
});
