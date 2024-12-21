# 사용자 생성 -> 인증 토큰 자동 생성

from django.db.models.signals import post_save      # Event 감지
from django.dispatch import receiver                # 수신자 설정
from rest_framework.authtoken.models import Token   # 사용자 인증 토큰 저장 모델
from django.conf import settings                    # 토큰 설정 불러오기

# post_save 신호 발생시마다 함수 발생
# 단, 사용자 모델이 저장된 후에 반응
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()