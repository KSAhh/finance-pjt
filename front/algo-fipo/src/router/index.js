import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import LoginView from "@/views/LoginView.vue";
import KakaoLogin from "@/components/KakaoLogin/KakaoLogin.vue";
import CallBack from "@/components/KakaoLogin/CallBack.vue";
import SignUpView from "@/views/SignUpView.vue";
import FindPasswordView from "@/views/FindPasswordView.vue";
import SavingsPage from "@/views/SavingsPage.vue";
import SavingDetail from "@/views/SavingDetail.vue";
import JoinForm from "@/components/Savings/SavingPage/JoinForm.vue";
import LoanPageView from "@/views/LoanPageView.vue";
import MyPageView from "@/views/MyPageView.vue";
import FAQView from "@/views/FAQView.vue";
import CustomerSupportView from "@/views/CustomerSupportView.vue";
import CustomerSupportDetailView from "@/views/CustomerSupportDetailView.vue";
import CSListCreate from "@/components/CustomerService/CSListCreate.vue"
import CustomerSupportEditView from "@/views/CustomerSupportEditView.vue"
import BankMapView from "@/views/BankMapView.vue";
import MyCommentsView from "@/views/MyCommentsView.vue";
import MyFinancialProductView from "@/views/MyFinancialProductView.vue";
import MyInquireView from "@/views/MyInquireView.vue";
import MyInfomationEditView from "@/views/MyInfomationEditView.vue";
import ContactManagement from "@/components/MyInfoEdit/ContactManagement.vue";
import PasswordEdit from "@/components/MyInfoEdit/PasswordEdit.vue";
import FinanceInfoEdit from "@/components/MyInfoEdit/FinanceInfoEdit.vue";
import DataAuthorization from "@/components/MyInfoEdit/DataAuthorization.vue";
import Notifications from "@/components/MyInfoEdit/Notifications.vue";
import AccountDeletion from "@/components/MyInfoEdit/AccountDeletion.vue";
import ExchangeView from "@/views/ExchangeView.vue"
import TopRates from "@/components/Savings/TopRates.vue";

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
    {
      path: "/find-password",
      name: "FindPassword",
      component: FindPasswordView,
    },
    {
      path: "/saving",
      name: "SavingsPage",
      component: SavingsPage,
    },
    {
      path: '/saving/:id',
      name: 'SavingsDetail',
      component: SavingDetail,
    },
    {
      path: '/join',
      name: 'JoinForm',
      component: JoinForm,
      meta: { requiresAuth: true }, // 로그인 필수 설정
    },
    {
      path: '/loans',
      name: 'LoanPage',
      component: LoanPageView,
    },
    {
      path: '/mypage',
      name: 'MyPage',
      component: MyPageView,
      meta: { requiresAuth: true }, // 로그인 필수 설정
    },
    {
      path: '/faq',
      name: 'FAQ',
      component: FAQView,
    },
    {
      path: '/cs',
      name: 'CustomerSupport',
      component: CustomerSupportView,
    },
    {
      path: '/cs/:article_pk',
      name: 'CustomerSupportDetail',
      component: CustomerSupportDetailView,
    },
    {
      path: '/cs/:article_pk/edit',
      name: 'CustomerSupportEditView',
      component: CustomerSupportEditView,
      meta: {requiresAuth: true }, // 로그인 필요
    },
    {
      path: '/cs/create',
      name: 'CSListCreate',
      component: CSListCreate,
      meta: {requiresAuth: true }, // 로그인 필요
    },
    {
      path: '/bankmap',
      name: 'BankMap',
      component: BankMapView,
    },
    {
      path: '/mycomments',
      name: 'MyComments',
      component: MyCommentsView,
      meta: { requiresAuth: true },
    },
    {
      path: '/myfinancialproduct',
      name: 'MyFinancialProduct',
      component: MyFinancialProductView,
      meta: { requiresAuth: true },
    },
    {
      path: '/myinquire',
      name: 'MyInquire',
      component: MyInquireView,
      meta: { requiresAuth: true },
    },
    {
      path: "/myinfoedit",
      name: "MyInfoEdit",
      component: MyInfomationEditView,
      meta: { requiresAuth: true }, // 인증 요구
    },
    {
      path: "/myinfoedit/contact-management",
      name: "ContactManagement",
      component: ContactManagement,
      meta: { requiresAuth: true },
    },
    {
      path: "/myinfoedit/password-edit",
      name: "PasswordEdit",
      component: PasswordEdit,
      meta: { requiresAuth: true },
    },
    {
      path: "/myinfoedit/finance-info-edit",
      name: "FinanceInfoEdit",
      component: FinanceInfoEdit,
      meta: { requiresAuth: true },
    },
    {
      path: "/myinfoedit/data-authorization",
      name: "DataAuthorization",
      component: DataAuthorization,
      meta: { requiresAuth: true },
    },
    {
      path: "/myinfoedit/notifications",
      name: "Notifications",
      component: Notifications,
      meta: { requiresAuth: true },
    },
    {
      path: "/myinfoedit/account-deletion",
      name: "AccountDeletion",
      component: AccountDeletion,
      meta: { requiresAuth: true },
    },
    {
      path: "/exchange-rate",
      name: "ExchangeView",
      component: ExchangeView,
    },
    {
      path: "/top-rates",
      name: "TopRates",
      component: TopRates,
    },
]});

router.beforeEach((to, from, next) => {
  const isLoggedIn = !!localStorage.getItem("key"); // 로그인 여부 확인 (key가 있는지 확인)

  if (to.meta.requiresGuest && isLoggedIn) {
    // 로그인 상태에서 로그인, 회원가입 페이지로 접근하려 하면 메인 페이지로 리다이렉트
    return next({ name: "MainView" });
  }

  if (to.meta.requiresAuth && !isLoggedIn) {
    // 로그인이 필요한 페이지에 접근하려고 하는데, 로그인되지 않은 경우
    return next({ name: "LoginView" });
  }
  next(); // 조건에 맞지 않는 경우 이동 허용
});


export default router;
