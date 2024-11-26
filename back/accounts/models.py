from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model

# from .managers import UserManager

# 유저
class User(AbstractUser):
    # 공통
    nickname = models.CharField(max_length=10)                        # 별명
    fullname = models.CharField(max_length=50)                        # 실명
    profile_image = models.ImageField(upload_to="profile_images/", default='profile_images/default.png')  # 프로필 이미지    
    date_joined = models.DateField(auto_now_add=True)                 # 가입일자
    deleted_at = models.DateTimeField(null=True, blank=True)          # 탈퇴 일자
    # 일반회원
    username = models.CharField(max_length=255, unique=True)          # 로그인ID
    password = models.CharField(max_length=255)                       # 비밀번호

    # 소셜회원
    email = models.EmailField(null=True, blank=True, default=None)    # 이메일


    def __str__(self):
        return self.nickname if self.nickname else f"User({self.username})" # 닉네임이 없으면 로그인 ID 반환


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[("남", "Male"), ("여", "Female")]) # 성별
    birth_date = models.DateField() # 출생일
    monthly_income = models.IntegerField() # 월 평균 소득
    monthly_expense = models.IntegerField() # 월 평균 소비
    total_assets = models.IntegerField()  # 총 자산
    is_mydata_consent = models.BooleanField(default=False) # 마이데이터 동의 여부

# allauth 유저 조회 - adapter 커스텀
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        email = data.get("email")
        username = data.get("username")
        # add fields
        nickname = data.get("nickname")
        fullname = data.get("fullname")
        profile_image = data.get("profile_image")

        user_email(user, email)
        user_username(user, username)
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
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
