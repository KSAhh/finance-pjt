from django.urls import path, include
from .views import KakaoLogin

app_name = 'accounts'

urlpatterns = [
    path('kakao/login/', KakaoLogin.as_view(), name='kakao_login'),
]
