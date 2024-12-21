"""
Django settings for algofipo_pjt project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 환경변수
import os
import environ
env = environ.Env(DEBUG=(bool, True))                           # 환경변수 저장 가능한 상태로 설정
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))   # 환경변수 읽어올 파일

KAKAO_API_KEY = env("KAKAO_API_KEY")                # 카카오로그인
DJANGO_SECRET_KEY = env("DJANGO_SECRET_KEY")
FSS_API_KEY = env("FSS_API_KEY")                                # 금융감독원
KAKAO_JS_KEY = env("KAKAO_JS_KEY")                              # 카카오 JS
KOREAEXIM_API_KEY = env("KOREAEXIM_API_KEY") # 한국수출입은행

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    # my app
    "accounts",
    "articles",
    "products",
    "exchange",
    
    # third party
    "corsheaders",               # CORS header

    # - DRF
    "rest_framework",            # serializer
    "rest_framework.authtoken",  # Token authentication
    
    # - REST_AUTH (signup)
    "dj_rest_auth",              # authentication library
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    "allauth.socialaccount",
    "django.contrib.sites",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.naver",
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# all_auth - related to social login
SITE_ID = 1  # registration

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id': KAKAO_API_KEY,  # Kakao Login REST API 키
            'secret': '', 
            "key": "",
        }
    }
}

# DRF auth settings
REST_FRAMEWORK = {
    # Authentication - Token
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    # permission
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],

    # 직렬화 과정에서 DecimalField를 문자열로 변환하지 않도록
    'COERCE_DECIMAL_TO_STRING': False, 

}

# REST-AUTH registration 기본 Serializer
REST_AUTH = {
    'REGISTER_SERIALIZER' : 'accounts.serializers.CustomRegisterSerializer',
    'USER_DETAILS_SERIALIZER' : 'accounts.serializers.CustomUserDetailsSerializer',
}
ACCOUNT_ADAPTER = 'accounts.models.CustomAccountAdapter'

# Django Allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # basic authentication
    'allauth.account.auth_backends.AuthenticationBackend', # allauth authentication
]

# Custom User
AUTH_USER_MODEL = "accounts.User"


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS header
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Add the account middleware
    "allauth.account.middleware.AccountMiddleware",  # authentication registration
]

# CORS header - 도메인 추가
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]
CORS_ALLOW_CREDENTIALS = True#

ROOT_URLCONF = "algofipo_pjt.urls"
# CSRF 관련 설정
CSRF_COOKIE_NAME = "csrftoken"  # CSRF 토큰이 저장될 쿠키 이름
CSRF_COOKIE_HTTPONLY = False  # JavaScript에서 쿠키에 접근할 수 있도록 False로 설정
CSRF_COOKIE_SECURE = False  # HTTPS 환경에서만 쿠키를 사용할지 여부 (개발 중에는 False)




TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "algofipo_pjt.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Media files (Images)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"