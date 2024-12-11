# 사용자 생성 -> 인증 토큰 자동 생성

from django.db.models.signals import post_save      # 모델 저장 이후 발생하는 신호(event)를 감지
from django.dispatch import receiver                # 신호를 처리할 수신자 설정
from rest_framework.authtoken.models import Token   # 인증 토큰 생성 및 관리하는 모델
from django.conf import settings                    # 프로젝트의 설정값 가져오기 (AUTH_USER_MODEL의 토큰설정 포함)

# post_save 신호를 수신
# 사용자 모델(AUTH_USER_MODEL)이 저장된 후에만 작동
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    사용자 모델 인스턴스가 처음 생성되었을 때 인증 토큰을 자동으로 생성.

    Args:
        sender: 신호를 발생시킨 모델 클래스 (AUTH_USER_MODEL)
        instance: 저장된 모델 인스턴스 (User 인스턴스)
        created: 새 객체가 생성된 경우 True, 그렇지 않으면 False
        **kwargs: 추가 매개변수
    """
    if created:  # 새 사용자 인스턴스가 생성된 경우에만 실행
        Token.objects.create(user=instance)  # 해당 사용자와 연결된 인증 토큰 생성
