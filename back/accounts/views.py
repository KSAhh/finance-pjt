from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# 회원가입 관련
from rest_framework.authtoken.models import Token
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter

# 회원탈퇴 및 정보수정 관련
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserProfileSerializer

from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()
temp_nickname_number = 0 # 유저명에 사용되는 임의값

# 유저탈퇴
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    """
    사용자 계정 삭제 (회원 탈퇴 처리)
    - 인증된 사용자만 요청 가능
    """
    user = request.user
    user.delete()
    return Response({"detail": "계정이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


# 카카오 로그인
class KakaoLogin(SocialLoginView):
    """
    카카오 소셜 로그인 및 회원가입 처리
    - 기존 사용자가 있으면 로그인
    - 없으면 신규 사용자 생성 후 로그인 처리
    """
    adapter_class = KakaoOAuth2Adapter

    def post(self, request):
        """
        POST /accounts/kakao/login/
        - 이메일과 닉네임(실명) 기반으로 사용자 계정 확인 및 처리
        """
        email = request.data.get("email")
        nickname = request.data.get("nickname")

        # 사용자 계정 확인
        user_qs = User.objects.filter(email=email)

        if user_qs.exists():
            # 기존 사용자와 소셜 계정 확인
            user = User.objects.get(email=email)
            social_user = SocialAccount.objects.filter(user=user).first()
            if social_user:
                # 기존 소셜 계정이 있는 경우: 로그인 성공 처리
                token = Token.objects.filter(user=user)
                token_data = token.values('key')
                return Response({'key': token_data, "detail": "로그인 성공하였습니다."}, status=status.HTTP_200_OK)
            
            if social_user is None:
                # 동일한 이메일로 소셜계정이 아닌, 일반계정으로 가입했을 때 처리 
                return Response({"detail": "동일한 이메일로 가입된 계정이 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
            
            if social_user.provider != "kakao":
                # 타 소셜계정으로 가입했을 때 처리
                return Response({"detail": "동일한 이메일로 타 소셜 계정에 가입되어 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
    
        else:
            # User Table에 계정 생성
            global temp_nickname_number
            new_user = User.objects.create(
                nickname=f"유저별명{temp_nickname_number}",
                email=email,
                fullname=nickname,
            )
            temp_nickname_number += 1

            # Social Account Table에 계정 생성
            SocialAccount.objects.create(user_id=new_user.id, provider='kakao')

            # 토큰 생성 - header로 전송
            token = Token.objects.create(user=new_user)
            return Response({'key': token.key, "detail": "회원가입 성공"}, status=status.HTTP_201_CREATED)


# 유저 금융자산
@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def assets(request):
    """
    사용자 금융 자산 관리
    - GET: 자산 조회
    - POST: 자산 등록
    - PUT: 자산 수정
    - DELETE: 자산 삭제
    """

    if request.method == "POST":
        if UserProfile.objects.filter(user=request.user).exists():
            # 이미 자산 정보가 등록되어 있는 경우
            return Response({"detail" : "이전에 작성된 프로필이 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "GET":
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        profile.delete()
        return Response({"detail": "자산정보가 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)