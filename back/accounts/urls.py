from django.urls import path, include
from .views import KakaoLogin
from . import views


app_name = 'accounts'

urlpatterns = [
    path("signup/", include("dj_rest_auth.registration.urls")),         # 일반 회원가입 
    path("delete/", views.delete_user, name="delete_user"),             # 일반 회원탈퇴
    path("kakao/login/", KakaoLogin.as_view(), name="kakao_login"),     # 카카오 소셜 회원가입/로그인
    path("assets/", views.assets, name="assets"),                       # 금융 자산 등록
]