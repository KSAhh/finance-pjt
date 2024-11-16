from django.db import models
from django.contrib.auth.models import AbstractUser


# 유저
# 필수 - nickname, email
# 자동 - .
# 관계 - .
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=150, unique=True, null=True, blank=False)  # 별명
    email = models.EmailField(unique=True)  # 이메일
    social_login_provider = models.CharField(max_length=50, null=False, default="")  # 소셜 로그인 제공자
    profile_image = models.ImageField(upload_to="profile_images/", null=False, default='profile_images/default.png')  # 프로필 이미지    
    is_social_user = models.BooleanField(default=False)  # 소셜 로그인 유저 여부
    deleted_at = models.DateTimeField(null=True, blank=True)  # 탈퇴 일자

    


