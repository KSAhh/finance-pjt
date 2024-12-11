from rest_framework import serializers

from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

UserModel = get_user_model()


# 회원가입 필드를 커스터마이징하는 시리얼라이저
class CustomRegisterSerializer(RegisterSerializer):
    """
    회원가입 시 사용자 입력을 위한 추가 필드를 정의하는 커스텀 시리얼라이저
    """
    # 추가 필드 정의
    nickname = serializers.CharField(required=True, allow_blank=False, max_length=10)
    fullname = serializers.CharField(required=True, allow_blank=False, max_length=50)
    profile_image = serializers.ImageField(required=False)
    
    def get_cleaned_data(self):
        """
        회원가입 데이터를 반환하는 메서드
        - 기존 RegisterSerializer의 get_cleaned_data를 오버라이드하여 추가 필드 처리
        """
        return {
            'username' : self.validated_data.get('username', ''),
            'password1' : self.validated_data.get('password1', ''),
            'nickname' : self.validated_data.get('nickname', ''),        
            'fullname' : self.validated_data.get('fullname', ''),        
            'profile_image' : self.validated_data.get('profile_image', ''),        
        }
    

# 유저 정보 조회용 시리얼라이저
class CustomUserDetailsSerializer(UserDetailsSerializer):
    """
    사용자 세부 정보를 조회할 때 사용되는 시리얼라이저
    - 기본 UserDetailsSerializer를 확장하여 커스텀 필드 추가
    """
    class Meta:
        extra_fields = []
        # User 모델의 속성 여부를 확인하여 필드 동적 추가
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'fullname'):
            extra_fields.append('fullname')
        if hasattr(UserModel, 'profile_image'):
            extra_fields.append('profile_image')

        model = UserModel
        fields = ('pk', *extra_fields) # 기본키와 동적 필드 포함
        read_only_fields = ('email', 'date_joined') # 읽기전용 필드
   
    def validate_profile_image(self, value):
        """
        프로필 이미지 유효성 검사
        """
        # 이미지 크기나 확장자 확인 등의 로직 추가 가능
        if value and not value.name.endswith(('.jpg', '.png', '.jpeg')):
            raise serializers.ValidationError("프로필 이미지는 JPG, PNG 형식만 허용됩니다.")
        return value


# 유저 금융 프로필 조회 및 관리용 시리얼라이저
class UserProfileSerializer(serializers.ModelSerializer):
    """
    UserProfile 모델 데이터를 처리하기 위한 시리얼라이저
    """
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = ["user"] # user 필드는 읽기 전용으로 설정