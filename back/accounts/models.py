from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model


# 사용자 테이블 - 회원 정보를 저장하는 커스텀 유저 모델
class User(AbstractUser):
    # 일반/소셜 회원 공통 필드
    nickname = models.CharField(max_length=10)                        # 별명
    fullname = models.CharField(max_length=50)                        # 실명
    profile_image = models.ImageField(upload_to="profile_images/", default='profile_images/default.png')  # 프로필 이미지 경로    
    date_joined = models.DateField(auto_now_add=True)                 # 가입일자
    deleted_at = models.DateTimeField(null=True, blank=True)          # 탈퇴일자 (soft delete 처리)

    # 일반 회원용 필드
    username = models.CharField(max_length=255, unique=True)          # 로그인ID
    password = models.CharField(max_length=255)                       # 비밀번호

    # 소셜 회원용 필드
    email = models.EmailField(null=True, blank=True, default=None)    # 이메일

    def __str__(self):
        """
        유저 반환시 별명을 우선 반환.
        별명이 없을 경우 username을 반환.
        """
        return self.nickname if self.nickname else f"User({self.username})"


# 마이데이터 테이블 - 유저의 개인 금융 정보와 관련된 추가 데이터 저장
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)             # User 모델과 1:1 관계
    gender = models.CharField(max_length=10, choices=[("남", "Male"), ("여", "Female")]) # 성별 (남/여))
    birth_date = models.DateField()                                                     # 출생일
    monthly_income = models.IntegerField()                                              # 월 평균 소득
    monthly_expense = models.IntegerField()                                             # 월 평균 소비
    total_assets = models.IntegerField()                                                # 총 자산
    is_mydata_consent = models.BooleanField(default=False)                              # 마이데이터 동의 여부


# Allauth 커스텀 어댑터 - 사용자 저장 방식을 커스터마이징
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        회원 가입 폼의 데이터를 기반으로 새로운 User 인스턴스를 저장.
        
        Args:
            request: HTTP 요청 객체
            user: 저장될 User 인스턴스
            form: 회원 가입 폼 데이터
            commit: 저장 여부 (True일 경우 DB에 즉시 저장)
        
        Returns:
            저장된 User 인스턴스
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        email = data.get("email")
        username = data.get("username")
        # 추가 필드 처리
        nickname = data.get("nickname")
        fullname = data.get("fullname")
        profile_image = data.get("profile_image")

        # 기본 필드 저장
        user_email(user, email)
        user_username(user, username)
        # 추가 필드 저장
        if nickname:
            user_field(user, "nickname", nickname)
        if fullname:
            user_field(user, "fullname", fullname)
        if profile_image:
            user_field(user, "profile_image", profile_image)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        # 유저 이름 자동 생성
        self.populate_username(request, user)
        if commit:
            user.save()
        return user