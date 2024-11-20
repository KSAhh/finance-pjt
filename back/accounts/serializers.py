from rest_framework import serializers

from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


UserModel = get_user_model()

# 회원가입 필드
class CustomRegisterSerializer(RegisterSerializer):
    # 필드 추가
    nickname = serializers.CharField(required=True, allow_blank=False, max_length=10)
    fullname = serializers.CharField(required=True, allow_blank=False, max_length=50)
    profile_image = serializers.ImageField(required=False)
    
    # 생성
    def get_cleaned_data(self):
        return {
            'username' : self.validated_data.get('username', ''),
            'password1' : self.validated_data.get('password1', ''),
            'nickname' : self.validated_data.get('nickname', ''),        
            'fullname' : self.validated_data.get('fullname', ''),        
            'profile_image' : self.validated_data.get('profile_image', ''),        
        }
    
    # 닉네임 중복방지
    # def validate_nickname(self, value):
    #     if User.objects.filter(nickname=value).exists():
    #         raise serializers.ValidationError("이미 사용 중인 닉네임입니다.")
    #     return value

# 유저 정보조회 필드
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
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
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)

# 회원정보 수정용
class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  # 비밀번호를 쓰기 전용으로 설정

    class Meta:
        model = UserModel
        fields = ['nickname', 'profile_image', 'password']

    def validate_password(self, value):
        """
        비밀번호를 해시화하여 저장
        """
        if value:  # 비밀번호가 요청에 포함된 경우
            return make_password(value)
        return value


