from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# 유저
class User(AbstractUser):
    # 공통
    nickname = models.CharField(max_length=150, unique=True)                        # 별명
    fullname = models.CharField(max_length=50)                                      # 실명
    profile_image = models.ImageField(upload_to="profile_images/", default='profile_images/default.png')  # 프로필 이미지    
    date_joined = models.DateField(auto_now_add=True)                               # 가입일자
    deleted_at = models.DateTimeField(null=True, blank=True)                        # 탈퇴 일자

    # 일반회원
    username = models.CharField(max_length=255, unique=True)                        # 로그인ID
    password = models.CharField(max_length=255)                                     # 비밀번호

    # 소셜회원
    email = models.EmailField(unique=True, null=True, blank=True, default=None)     # 이메일

    # 커스텀 매니저 연결
    objects = UserManager()  

    def __str__(self):
        return self.nickname if self.nickname else f"User({self.username})"         # 닉네임이 없으면 로그인 ID 반환
