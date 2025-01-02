from django.urls import path, include
from .views import (
    KakaoLogin, DeleteUserView, UpdateUserView,
    check_survey_status, submit_survey
)
from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/", include("dj_rest_auth.registration.urls")),  # 일반 회원가입
    path("delete/", DeleteUserView.as_view(), name="delete_user"),  # 회원탈퇴
    path("update/", UpdateUserView.as_view(), name="update_user"),  # 회원정보 수정
    path("kakao/login/", KakaoLogin.as_view(), name="kakao_login"), # 카카오 로그인
    path("assets/", views.assets, name="assets"),                  # 금융자산 등록
    path("check-id/", views.check_id, name="check_id"),            # 아이디 중복 체크
    path("get-csrf-token/", views.get_csrf_token_view, name="get_csrf_token"),
    
    # 설문 상태 확인: GET
    path("check-survey-status/", check_survey_status, name="check_survey_status"),

    # 설문 데이터 저장: POST
    path("submit-survey/", submit_survey, name="submit_survey"),
]
