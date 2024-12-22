# accounts/serializers.py
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import UserProfile

UserModel = get_user_model()

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from .models import UserProfile

UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    # User 모델 필드
    nickname = serializers.CharField(required=True, allow_blank=False, max_length=10)
    fullname = serializers.CharField(required=True, allow_blank=False, max_length=50)
    profile_image = serializers.ImageField(required=False, allow_null=True)
    
    # UserProfile 모델 필드
    gender = serializers.ChoiceField(
        choices=[("남", "Male"), ("여", "Female")],
        required=True
    )
    birth_date = serializers.DateField(required=True)  # 출생일 필수
    monthly_income = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
    monthly_expense = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
    total_assets = serializers.DecimalField(max_digits=15, decimal_places=2, required=True)
    is_mydata_consent = serializers.BooleanField(default=False, required=False)
    job = serializers.ChoiceField(
        choices=[
            ("직장인", "Office Worker"),
            ("자영업자", "Self-Employed"),
            ("학생", "Student"),
            ("무직", "Unemployed"),
            ("기타", "Other"),
        ],
        required=True,
    )
    category_choice = serializers.ChoiceField(
        choices=[
            (1, "정액적립식 복리"),
            (2, "자유적립식 단리"),
            (3, "정기예금 단리"),
            (4, "정기예금 복리")
        ],
        required=False,
        allow_null=True
    )
    has_main_bank = serializers.BooleanField(required=False, allow_null=True)
    change_bank = serializers.BooleanField(required=False, allow_null=True)
    max_contract_months = serializers.IntegerField(required=False, allow_null=True)
    interest_in_event = serializers.BooleanField(required=False, allow_null=True)
    deposit_min = serializers.DecimalField(max_digits=15, decimal_places=2, required=False, allow_null=True)
    deposit_max = serializers.DecimalField(max_digits=15, decimal_places=2, required=False, allow_null=True)
    saving_min = serializers.DecimalField(max_digits=15, decimal_places=2, required=False, allow_null=True)
    saving_max = serializers.DecimalField(max_digits=15, decimal_places=2, required=False, allow_null=True)

    def validate_birth_date(self, value):
        """birth_date가 누락되었거나 유효하지 않을 경우 검증"""
        if not value:
            raise serializers.ValidationError("출생일은 필수 입력 항목입니다.")
        return value

    def get_cleaned_data(self):
        """User 및 UserProfile 데이터를 반환"""
        data = super().get_cleaned_data()
        data.update({
            'nickname': self.validated_data.get('nickname', ''),
            'fullname': self.validated_data.get('fullname', ''),
            'profile_image': self.validated_data.get('profile_image', None),
            'gender': self.validated_data.get('gender', None),
            'birth_date': self.validated_data.get('birth_date', None),
            'monthly_income': self.validated_data.get('monthly_income', None),
            'monthly_expense': self.validated_data.get('monthly_expense', None),
            'total_assets': self.validated_data.get('total_assets', None),
            'is_mydata_consent': self.validated_data.get('is_mydata_consent', False),
            'job': self.validated_data.get('job', None),
            'category_choice': self.validated_data.get('category_choice', None),
            'has_main_bank': self.validated_data.get('has_main_bank', None),
            'change_bank': self.validated_data.get('change_bank', None),
            'max_contract_months': self.validated_data.get('max_contract_months', None),
            'interest_in_event': self.validated_data.get('interest_in_event', None),
            'deposit_min': self.validated_data.get('deposit_min', None),
            'deposit_max': self.validated_data.get('deposit_max', None),
            'saving_min': self.validated_data.get('saving_min', None),
            'saving_max': self.validated_data.get('saving_max', None),
        })
        return data

    def save(self, request):
        try:
            user = super().save(request)
            user.nickname = self.validated_data.get('nickname')
            user.fullname = self.validated_data.get('fullname')
            if self.validated_data.get('profile_image'):
                user.profile_image = self.validated_data.get('profile_image')
            user.save()

            # UserProfile 업데이트
            profile, created = UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    "birth_date": self.validated_data.get('birth_date'),
                    "gender": self.validated_data.get('gender'),
                    "monthly_income": self.validated_data.get('monthly_income'),
                    "monthly_expense": self.validated_data.get('monthly_expense'),
                    "total_assets": self.validated_data.get('total_assets'),
                    "is_mydata_consent": self.validated_data.get('is_mydata_consent', False),
                    "job": self.validated_data.get('job'),
                    "category_choice": self.validated_data.get('category_choice'),
                    "has_main_bank": self.validated_data.get('has_main_bank'),
                    "change_bank": self.validated_data.get('change_bank'),
                    "max_contract_months": self.validated_data.get('max_contract_months'),
                    "interest_in_event": self.validated_data.get('interest_in_event'),
                    "deposit_min": self.validated_data.get('deposit_min'),
                    "deposit_max": self.validated_data.get('deposit_max'),
                    "saving_min": self.validated_data.get('saving_min'),
                    "saving_max": self.validated_data.get('saving_max'),
                },
            )
            print(f"Profile saved: {profile}, Created: {created}")  # 디버깅용 로그
            return user

        except Exception as e:
            raise serializers.ValidationError(f"오류 발생: {str(e)}")

# 유저 정보 조회 시리얼라이저
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'nickname', 'fullname', 'profile_image', 'date_joined')
        read_only_fields = ('email', 'date_joined')

# 회원정보 수정용 시리얼라이저
class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_null=True)
    
    class Meta:
        model = UserModel
        fields = ['nickname', 'profile_image', 'password']
    
    def validate_password(self, value):
        """
        비밀번호를 해시화하여 저장
        """
        if value:
            return make_password(value)
        return value
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.password = password
        instance.save()
        return instance

# 유저 금융 프로필 시리얼라이저
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = ["user"]
