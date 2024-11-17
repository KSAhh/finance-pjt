import { createRouter, createWebHistory } from "vue-router";
import KakaoLogin from "@/components/KakaoLogin.vue";
import Callback from "@/components/Callback.vue";

const routes = [
  {
    path: "/kakao-login",
    name: "KakaoLogin",
    component: KakaoLogin,
  },
  {
    path: "/callback",
    name: "Callback",
    component: Callback,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
