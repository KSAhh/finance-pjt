from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# 회원가입
from rest_framework.authtoken.models import Token
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter

# 회원탈퇴/정보수정
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UpdateUserSerializer, UserProfileSerializer
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth import get_user_model

from .models import UserProfile

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.middleware.csrf import get_token
from django.utils import timezone
import uuid

User = get_user_model()

# 유저탈퇴
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        # Soft Deletion
        user.deleted_at = timezone.now()
        user.is_active = False
        user.save()
        return Response({"detail": "Account has been deactivated."}, status=status.HTTP_200_OK)


# 유저 정보 변경
class UpdateUserView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserSerializer
    http_method_names = ['patch']

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(instance=self.get_object(), data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        # UserProfile 업데이트
        profile_serializer = UserProfileSerializer(instance=request.user.profile, data=request.data, partial=True)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        return Response({
            "user": user_serializer.data,
            "profile": profile_serializer.data
        }, status=status.HTTP_200_OK)


# 카카오 로그인
class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        nickname = request.data.get("nickname")

        if not email or not nickname:
            return Response({"detail": "이메일과 닉네임은 필수입니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            social_user = SocialAccount.objects.filter(user=user, provider='kakao').first()
            if social_user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'key': token.key, "detail": "로그인 성공"}, status=status.HTTP_200_OK)

            if SocialAccount.objects.filter(user=user).exclude(provider='kakao').exists():
                return Response({"detail": "동일한 이메일로 다른 소셜 계정이 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)

            # 소셜 계정이 없을 때
            return Response({"detail": "소셜 계정이 연결되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            # 새로운 사용자 생성
            unique_nickname = f"나는유저{uuid.uuid4().hex[:8]}"
            new_user = User.objects.create(
                nickname=unique_nickname,
                email=email,
                fullname=nickname,
            )
            new_user.set_unusable_password()
            new_user.save()

            SocialAccount.objects.create(user=new_user, provider='kakao')

            token = Token.objects.create(user=new_user)
            return Response({'key': token.key, "detail": "회원가입 성공"}, status=status.HTTP_201_CREATED)


# 유저 금융자산
@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def assets(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "GET":
        # 유저 정보 조회
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method in ["PATCH", "PUT"]:
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        profile.delete()
        return Response({"detail": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def check_id(request):
    try:
        username = request.data.get("username", "")
        if not username:
            return Response({"error": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)

        is_duplicate = User.objects.filter(username=username).exists()
        return Response({"is_duplicate": is_duplicate}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_csrf_token_view(request):
    return Response({'csrfToken': get_token(request)}, status=status.HTTP_200_OK)
