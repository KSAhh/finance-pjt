from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# 사용자 생성 시 인증 토큰 자동 생성
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# UserProfile 관련 시그널 제거
# UserProfile 생성/업데이트는 CustomAccountAdapter에서 처리
