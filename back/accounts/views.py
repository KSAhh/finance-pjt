<<<<<<< HEAD
from rest_framework import status, generics
from rest_framework.response import Response

# 회원가입
=======
from rest_framework import status, generics # API View Custom
from rest_framework.response import Response

from rest_framework.permissions import AllowAny
>>>>>>> feat/front/main+cs
from rest_framework.authtoken.models import Token
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter

<<<<<<< HEAD
# 회원탈퇴/정보수정
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UpdateUserSerializer

from django.contrib.auth import get_user_model

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
=======
from .serializers import SignupSerializer
from django.contrib.auth import get_user_model


User = get_user_model()
temp_nickname_number = 0 # 유저명에 사용되는 임의값


>>>>>>> feat/front/main+cs
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
<<<<<<< HEAD
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
=======
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'key': token.key, "message": "로그인 성공"}, status=status.HTTP_200_OK)
            
            # 동일한 이메일의 유저가 있지만, social계정이 아닐때 
            if social_user is None:
                return Response({"message": "동일한 이메일로 가입된 소셜 계정이 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
            
            # 소셜계정이 카카오가 아닌 다른 소셜계정으로 가입했을때
            if social_user.provider != "kakao":
                return Response({"message": "동일한 이메일로 타 소셜 계정에 가입되어 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> feat/front/main+cs
    
        # 기존에 가입된 유저가 없으면 새로 가입
        except User.DoesNotExist:
            
<<<<<<< HEAD
            # User Table에 계정 생성
=======
            # User Table에 게정 생성
>>>>>>> feat/front/main+cs
            global temp_nickname_number
            new_user = User.objects.create(
                nickname=f"나는유저{temp_nickname_number}",
                email=email,
                fullname=nickname,
            )
            temp_nickname_number += 1

            # Social Account Table에 계정 생성
            SocialAccount.objects.create(user_id=new_user.id, provider='kakao')

<<<<<<< HEAD
            # 토큰 생성 - header로 전송
            
            token = Token.objects.create(user=new_user)
            return Response({'key': token.key, "detail": "회원가입 성공"}, status=status.HTTP_201_CREATED)
=======
            # 토큰 생성
            token = Token.objects.create(user=new_user)
            return Response({'key': token.key, "message": "회원가입 성공"}, status=status.HTTP_201_CREATED)


# 회원가입 API View 커스텀
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()           # DB에 작업할 모델 쿼리셋 지정
    serializer_class = SignupSerializer     # 요청 데이터 검증, 반환 시리얼라이저
    permission_classes = [AllowAny]         # 유저객체 접근 권한

    def create(self, request, *args, **kwargs):
        # request.data : QueryDict / 클라이언트로 부터 받은 요청 데이터
        data = request.data.copy()                      # QueryDict를 복사하여 수정 가능하도록 처리 (이메일 제외 위함)
        if not data.get("email"):
            data["email"] = None                        # 이메일 필드를 None으로 설정
            serializer = self.get_serializer(data=data) # serializer 객체 반환
        serializer.is_valid(raise_exception=True)       # 유효성 검증

        response = super().create(request, *args, **kwargs)         # DB에 유저객체 생성후, HTTP 응답객체 반환
        user = User.objects.get(username=response.data["username"]) # 생성된 사용자 가져오기
        token, created = Token.objects.get_or_create(user=user)     # 생성된 토큰 가져오기
        
        # 응답 데이터에 토큰 추가
        response_data = response.data
        response_data["key"] = token.key
        response_data["message"] = "회원가입 성공"
        return Response(response_data, status=status.HTTP_201_CREATED)
>>>>>>> feat/front/main+cs
