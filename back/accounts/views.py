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

# 설문조사 데이터 저장 API
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_survey(request):
    user = request.user
    data = request.data

    # partial=True로 부분 업데이트 허용
    from .serializers import UserProfileSerializer
    serializer = UserProfileSerializer(data=data, partial=True)
    if serializer.is_valid():
        UserProfile.objects.update_or_create(user=user, defaults=serializer.validated_data)
        return Response({"detail": "설문조사가 성공적으로 저장되었습니다."}, status=201)
    return Response(serializer.errors, status=400)



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

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import UserProfile

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def check_survey_status(request):
    user = request.user
    user_profile = UserProfile.objects.filter(user=user).first()

    required_fields = [
        "gender", "birth_date", "monthly_income", "monthly_expense",
        "total_assets", "is_mydata_consent", "job", "category_choice",
        "has_main_bank", "change_bank", "max_contract_months",
        "interest_in_event", "deposit_min", "deposit_max",
        "saving_min", "saving_max",
    ]

    print("DEBUG: check_survey_status called")
    print("DEBUG: user =", user.username, " / user_profile exists =", bool(user_profile))

    if not user_profile:
        print("DEBUG: user_profile does not exist. All fields are considered missing.")
        return Response({
            "requires_survey": True,
            "message": "설문조사를 진행해주세요.",
            "missing_fields": required_fields,
        }, status=200)

    missing_fields = []

    # 모든 필드값 찍어보기
    print("DEBUG: Current profile field values:")
    for fld in required_fields:
        print(f"   {fld} =", getattr(user_profile, fld, None))

    for field in required_fields:
        value = getattr(user_profile, field, None)

        # 1) 숫자(Decimal, Integer) 필드: 0은 정상, None은 누락
        if field in [
            "monthly_income", "monthly_expense", "total_assets",
            "deposit_min", "deposit_max", "saving_min", "saving_max"
        ]:
            if value is None:
                missing_fields.append(field)

        # 2) Boolean 필드: None이면 누락, False는 정상 입력
        elif field in [
            "is_mydata_consent", "has_main_bank", "change_bank", "interest_in_event"
        ]:
            if value is None:
                missing_fields.append(field)

        # 3) 나머지(문자, 날짜 등): if not value => 누락
        else:
            if not value:  # "", None, False 모두 누락
                missing_fields.append(field)

    print("DEBUG: computed missing_fields ->", missing_fields)

    if missing_fields:
        print("DEBUG: requires_survey = True (fields missing)")
        return Response({
            "requires_survey": True,
            "message": "설문조사를 진행해주세요.",
            "missing_fields": missing_fields,
        }, status=200)

    print("DEBUG: requires_survey = False (no missing fields)")
    return Response({"requires_survey": False}, status=200)



class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get("email")
            nickname = request.data.get("nickname")

            # 기존 유저 확인
            user = User.objects.filter(email=email).first()

            if user:
                # 닉네임이 비어 있으면 fullname으로 대체
                if not user.nickname or user.nickname.strip() == "":
                    if user.fullname and user.fullname.strip() != "":
                        user.nickname = user.fullname
                        user.save()

                # 토큰 생성(기존 유저)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "is_existing_user": True,
                    "token": token.key,
                    "detail": "로그인에 성공했습니다.",
                }, status=status.HTTP_200_OK)

            # 신규 유저 생성
            temp_user = User.objects.create(
                email=email,
                fullname=nickname,
                nickname=nickname,
                username=f"kakao_{uuid.uuid4().hex[:8]}"
            )
            temp_user.set_unusable_password()
            temp_user.save()

            # 신규 유저도 토큰 발급
            new_token = Token.objects.create(user=temp_user)

            return Response({
                "is_existing_user": False,
                "token": new_token.key,
                "email": temp_user.email,
                "nickname": temp_user.nickname,
                "detail": "새 계정이 생성되었습니다.",
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "detail": f"요청 처리 중 오류가 발생했습니다: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




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
