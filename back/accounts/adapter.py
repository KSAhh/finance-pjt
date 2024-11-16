from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        """
        사용자 정보 저장 전에 추가 정보를 요구
        """
        user = sociallogin.user

        # 이메일 또는 닉네임 등 필수 값이 없는 경우 추가 입력 요구
        if not user.email or not user.nickname:
            raise ValueError("사용자 이메일 또는 닉네임이 필요합니다.")

        return super().save_user(request, sociallogin, form)
