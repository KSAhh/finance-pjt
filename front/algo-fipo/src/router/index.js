import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import LoginView from "@/views/LoginView.vue";
import KakaoLogin from "@/components/KakaoLogin/KakaoLogin.vue";
import CallBack from "@/components/KakaoLogin/CallBack.vue";
import SignUpView from "@/views/SignUpView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "MainView",
      component: MainView,
    },
    {
      path: "/login",
      name: "LoginView",
      component: LoginView,
      meta: { requiresGuest: true }, // 비로그인 사용자만 접근 가능
    },
    {
      path: "/kakao-login",
      name: "KakaoLogin",
      component: KakaoLogin,
    },
    {
      path: "/Kakao/login/callback",
      name: "KakaoLoginCallBack",
      component: CallBack,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
      meta: { requiresGuest: true }, // 비로그인 사용자만 접근 가능
    },
  ],
});

router.beforeEach((to, from, next) => {
  const isLoggedIn = !!localStorage.getItem("key"); // 로그인 여부 확인 (key가 있는지 확인)

  if (to.meta.requiresGuest && isLoggedIn) {
    // 로그인 상태에서 로그인, 회원가입 페이지로 접근하려 하면 메인 페이지로 리다이렉트
    return next({ name: "MainView" });
  }

  next(); // 조건에 맞지 않는 경우 이동 허용
});

export default router;
