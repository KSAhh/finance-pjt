from django.contrib import admin
from django.urls import path, include

# Media 파일 서빙 설정 (개발 환경)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path("admin/", admin.site.urls),                        # Django 기본 관리 페이지

    # Authentication
    path("accounts/", include("accounts.urls")),            # 사용자 관리: 회원가입, 소셜 로그인, 회원탈퇴
    path("accounts/", include("dj_rest_auth.urls")),        # 인증 : 로그인, 로그아웃, 비밀번호 변경, 회원정보 변경

    # Articles API
    path("api/v1/articles/", include("articles.urls")),     # 게시물 관련 API (CRUD)

    # Products API  
    path("api/v1/products/", include("products.urls")),     # 상품 관련 API (상품 조회, 가입)

    # exchange API
    path("api/v1/exchange/", include("exchange.urls")),     # 환율 관련 API (환율 정보 조회, 계산)
]

# Media 파일 서빙 (개발 환경에서만 사용)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)