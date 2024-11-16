from django.urls import path
from . import views
from .views import KakaoLogin

app_name = 'accounts'

urlpatterns = [
    path('kakao/login/', KakaoLogin.as_view(), name='kakao_login'),

    # path('', views.index, name='index'),
    # path('login/', views.login, name='login'), # 유저 로그인
    # path('logout/', views.logout, name='logout'), # 유저 로그아웃
    # path('signup/', views.signup, name='signup'), # 유저 회원가입
    # path('signout/', views.signout, name='signout'), # 유저 탈퇴
    # path('update/', views.update, name='update'), # 유저 정보수정
]
