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
    path('admin/', admin.site.urls),

    # Articles API
    path('api/v1/', include('articles.urls')),

    # Authentication
    path("accounts/", include("dj_rest_auth.urls")),  # 로그인, 로그아웃, 비밀번호 변경 등
    path("accounts/signup/", include("dj_rest_auth.registration.urls")),  # 회원가입 관련 URL
    path('accounts/social/', include('accounts.urls')),
    path("accounts/allauth/", include("allauth.urls")),  

    # path('accounts/', include('accounts.urls')),
    # path('accounts/', include('allauth.urls')),
    # path("accounts/social/", include("allauth.urls")),  # 소셜 로그인 URL (allauth)
    # path("accounts/kakao/", include("allauth.socialaccount.urls")),  # 소셜 로그인
    # path("api/social/", include("allauth.socialaccount.urls")),  # 소셜 로그인

    # path('api-auth/', include('rest_framework.urls')), # DRF 기본 인증뷰 (세션인증)
    # path('<int:user_pk>/password/', accounts_views.update_password, name='update_password'), # 유저 비밀번호 변경

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
