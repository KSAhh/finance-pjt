from django.urls import path, include
from .views import KakaoLogin, DeleteAccountView
app_name = 'accounts'

urlpatterns = [
    path("signup/", include("dj_rest_auth.registration.urls")),         # 일반 회원가입 
    path("signout/", DeleteAccountView.as_view(), name="singout"),      # 일반 회원탈퇴
    path('kakao/login/', KakaoLogin.as_view(), name="kakao_login"),     # 소셜 회원가입 
]