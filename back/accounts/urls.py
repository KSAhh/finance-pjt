from django.urls import path, include
from .views import KakaoLogin, DeleteUserView, UpdateUserView

app_name = 'accounts'

urlpatterns = [
    path("signup/", include("dj_rest_auth.registration.urls")),         # 일반 회원가입 
    path("delete/", DeleteUserView.as_view(), name="delete_user"),      # 일반 회원탈퇴
    path("update/", UpdateUserView.as_view(), name="update_user"),          # 회원 정보수정
    path('kakao/login/', KakaoLogin.as_view(), name="kakao_login"),     # 소셜 회원가입 
]
