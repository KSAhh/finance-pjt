from django.urls import path, include
from .views import KakaoLogin, SignupView

app_name = 'accounts'

urlpatterns = [
    path('kakao/login/', KakaoLogin.as_view(), name='kakao_login'),
    path("signup/", SignupView.as_view(), name="signup"),
]
