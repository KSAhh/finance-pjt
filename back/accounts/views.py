from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404, render

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
User = get_user_model()


# 유저탈퇴
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()  # 계정을 완전히 삭제
        return Response({"detail": "Account has been deleted."}, status=status.HTTP_204_NO_CONTENT)


# 유저 정보 변경
class UpdateUserView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserSerializer
    http_method_names = ['patch'] # PATCH 메서드만 허용

    def get_object(self):
        return self.request.user  # 현재 로그인한 사용자


temp_nickname_number = 0 # 유저명에 사용되는 임의값

# 카카오 로그인
class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

    def post(self, request):
        email = request.data.get("email")
        nickname = request.data.get("nickname")
        try:
            # 기존에 가입된 유저와 쿼리해서 존재하면서, SocialAccount에도 존재하면 로그인
            user = User.objects.get(email=email)
            social_user = SocialAccount.objects.filter(user=user).first()
            # 로그인
            if social_user:
                # 이미 존재하는 사용자 -> 토큰 생성 또는 가져오기
                token = Token.objects.filter(user=user)
                token_data = token.values('key')
                print(token.values('key'))
                return Response({'key': token_data, "detail": "로그인 성공"}, status=status.HTTP_200_OK)
            
            # 동일한 이메일의 유저가 있지만, social계정이 아닐때 
            if social_user is None:
                return Response({"detail": "동일한 이메일로 가입된 소셜 계정이 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
            
            # 소셜계정이 카카오가 아닌 다른 소셜계정으로 가입했을때
            if social_user.provider != "kakao":
                return Response({"detail": "동일한 이메일로 타 소셜 계정에 가입되어 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
    
        # 기존에 가입된 유저가 없으면 새로 가입
        except User.DoesNotExist:
            
            # User Table에 계정 생성
            global temp_nickname_number
            new_user = User.objects.create(
                nickname=f"나는유저{temp_nickname_number}",
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
@api_view(["GET", "PUT", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def assets(request):

    if request.method == "POST":
        # 유저 정보 작성
        if UserProfile.objects.filter(user=request.user).exists():
            return Response({"detail" : "이전에 작성된 프로필이 존재합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "GET":
        # 유저 정보 조회
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        profile.delete()
        return Response({"detail": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)