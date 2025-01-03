"""
URL configuration for algofipo_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication
    path("accounts/", include("accounts.urls")),            # 소셜 로그인, 회원가입, 회원탈퇴
    path("accounts/", include("dj_rest_auth.urls")),        # 로그인, 로그아웃, 비밀번호 변경 등
    # path("api-auth/", include("rest_framework.urls")),    # DRF 기본 인증뷰 (세션인증)

    # Articles API
    path("api/v1/articles/", include("articles.urls")),

    # Products API
    path("api/v1/products/", include("products.urls")),

    # exchange API
    path("api/v1/exchange/", include("exchange.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)