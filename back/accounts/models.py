from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model

# 유저 모델
class User(AbstractUser):
    first_name = None  # Django 기본 필드 제거
    last_name = None   # Django 기본 필드 제거
    # 공통 필드
    nickname = models.CharField(max_length=10)  # 별명
    fullname = models.CharField(max_length=50)  # 실명
    profile_image = models.ImageField(upload_to="profile_images/", default='profile_images/default.png')  # 프로필 이미지    
    date_joined = models.DateField(auto_now_add=True)  # 가입일자
    deleted_at = models.DateTimeField(null=True, blank=True)  # 탈퇴 일자
    # 일반회원 필드
    username = models.CharField(max_length=255, unique=True)  # 로그인ID
    password = models.CharField(max_length=255)  # 비밀번호
    # 소셜회원 필드
    email = models.EmailField(null=True, blank=True, default=None)  # 이메일

    def __str__(self):
        return self.nickname if self.nickname else f"User({self.username})"  # 닉네임이 없으면 로그인 ID 반환

from django.db import models
from django.contrib.auth import get_user_model

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, choices=[("남", "Male"), ("여", "Female")])  # 성별
    birth_date = models.DateField(null=False, blank=True)  # 출생일
    monthly_income = models.DecimalField(max_digits=15, decimal_places=2)  # 월 평균 소득
    monthly_expense = models.DecimalField(max_digits=15, decimal_places=2)  # 월 평균 소비
    total_assets = models.DecimalField(max_digits=15, decimal_places=2)  # 총 자산
    is_mydata_consent = models.BooleanField(default=False)  # 마이데이터 동의 여부
    job = models.CharField(
        max_length=50,
        choices=[
            ("직장인", "Office Worker"),
            ("자영업자", "Self-Employed"),
            ("학생", "Student"),
            ("무직", "Unemployed"),
            ("기타", "Other"),
        ],
        null=True,
        blank=True,
        verbose_name="직업"
    )
    category_choice = models.IntegerField(
        choices=[
            (1, "정액적립식 복리"),
            (2, "자유적립식 단리"),
            (3, "정기예금 단리"),
            (4, "정기예금 복리")
        ],
        null=True, blank=True, verbose_name="관심 카테고리"
    )

    # Step 3 데이터
    has_main_bank = models.BooleanField(null=True, blank=True, verbose_name="주거래 은행 여부")
    change_bank = models.BooleanField(null=True, blank=True, verbose_name="주거래 은행 변경 의향")
    max_contract_months = models.IntegerField(null=True, blank=True, verbose_name="최대 계약 기간 (개월)")
    interest_in_event = models.BooleanField(null=True, blank=True, verbose_name="이벤트 상품 관심 여부")  # Boolean 처리
    deposit_min = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="정기예금 최소 금액")
    deposit_max = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="정기예금 최대 금액")
    saving_min = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="정기적금 최소 금액")
    saving_max = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="정기적금 최대 금액")

    def __str__(self):
        return f"{self.user.username} - Profile"


# class UserProfile(models.Model):
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#     gender = models.CharField(max_length=10, choices=[("남", "Male"), ("여", "Female")])  # 성별
#     birth_date = models.DateField()  # 출생일
#     monthly_income = models.IntegerField()  # 월 평균 소득
#     monthly_expense = models.IntegerField()  # 월 평균 소비
#     total_assets = models.IntegerField()  # 총 자산
#     is_mydata_consent = models.BooleanField(default=False)  # 마이데이터 동의 여부
#     job = models.CharField(
#         max_length=50,
#         choices=[
#             ("직장인", "Office Worker"),
#             ("자영업자", "Self-Employed"),
#             ("학생", "Student"),
#             ("무직", "Unemployed"),
#             ("기타", "Other"),
#         ],
#         null=True,
#         blank=True,
#         verbose_name="직업"
#     )
#     category_choice = models.IntegerField(
#         choices=[
#             (1, "정액적립식 복리"),
#             (2, "자유적립식 단리"),
#             (3, "정기예금 단리"),
#             (4, "정기예금 복리")
#         ],
#         null=True, blank=True, verbose_name="관심 카테고리"
#     )

#     # Step 3 데이터
#     has_main_bank = models.BooleanField(null=True, blank=True, verbose_name="주거래 은행 여부")
#     change_bank = models.BooleanField(null=True, blank=True, verbose_name="주거래 은행 변경 의향")
#     max_contract_months = models.IntegerField(null=True, blank=True, verbose_name="최대 계약 기간 (개월)")
#     interest_in_event = models.BooleanField(null=True, blank=True, verbose_name="이벤트 상품 관심 여부")  # 수정된 필드
#     deposit_min = models.IntegerField(null=True, blank=True, verbose_name="정기예금 최소 금액")
#     deposit_max = models.IntegerField(null=True, blank=True, verbose_name="정기예금 최대 금액")
#     saving_min = models.IntegerField(null=True, blank=True, verbose_name="정기적금 최소 금액")
#     saving_max = models.IntegerField(null=True, blank=True, verbose_name="정기적금 최대 금액")

#     def __str__(self):
#         return f"{self.user.username} - Profile"



from .models import UserProfile

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.email = data.get("email")
        user.username = data.get("username")
        user.nickname = data.get("nickname", "")
        user.fullname = data.get("fullname", "")
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
            # UserProfile 생성/업데이트
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    "birth_date": data.get("birth_date"),
                    "gender": data.get("gender"),
                    "monthly_income": data.get("monthly_income"),
                    "monthly_expense": data.get("monthly_expense"),
                    "total_assets": data.get("total_assets"),
                    "job": data.get("job"),
                    "category_choice": data.get("category_choice"),
                    "has_main_bank": data.get("has_main_bank"),
                    "change_bank": data.get("change_bank"),
                    "max_contract_months": data.get("max_contract_months"),
                    "interest_in_event": data.get("interest_in_event"),
                    "deposit_min": data.get("deposit_min"),
                    "deposit_max": data.get("deposit_max"),
                    "saving_min": data.get("saving_min"),
                    "saving_max": data.get("saving_max"),
                },
            )
        return user




# # allauth 유저 조회 - adapter 커스텀
# class CustomAccountAdapter(DefaultAccountAdapter):
#     def save_user(self, request, user, form, commit=True):
#         from allauth.account.utils import user_email, user_field, user_username
#         data = form.cleaned_data
#         email = data.get("email")
#         username = data.get("username")
#         nickname = data.get("nickname")
#         fullname = data.get("fullname")
#         profile_image = data.get("profile_image")
#         category_choice = data.get("category_choice")
#         has_main_bank = data.get("has_main_bank")
#         change_bank = data.get("change_bank")
#         max_contract_months = data.get("max_contract_months")
#         interest_in_event = data.get("interest_in_event")  # Boolean 처리
#         deposit_min = data.get("deposit_min")
#         deposit_max = data.get("deposit_max")
#         saving_min = data.get("saving_min")
#         saving_max = data.get("saving_max")

#         user_email(user, email)
#         user_username(user, username)
#         if nickname:
#             user_field(user, "nickname", nickname)
#         if fullname:
#             user_field(user, "fullname", fullname)
#         if profile_image:
#             user_field(user, "profile_image", profile_image)
#         if "password1" in data:
#             user.set_password(data["password1"])
#         else:
#             user.set_unusable_password()
#         self.populate_username(request, user)
#         if commit:
#             user.save()
#             UserProfile.objects.create(
#                 user=user,
#                 category_choice=category_choice,
#                 has_main_bank=has_main_bank,
#                 change_bank=change_bank,
#                 max_contract_months=max_contract_months,
#                 interest_in_event=interest_in_event,  # Boolean 데이터 저장
#                 deposit_min=deposit_min,
#                 deposit_max=deposit_max,
#                 saving_min=saving_min,
#                 saving_max=saving_max,
#             )
#         return user

