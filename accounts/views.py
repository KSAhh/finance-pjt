from django.shortcuts import render, redirect

# 유저 정보 관련
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash # 세션 무효화 방지 (선택)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm # 로그인, 비밀번호 변경
from .forms import CustomUserCreationForm # 유저 생성
from .forms import CustomUserChangeForm # 유저 정보변경
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'accounts/index.html')

def login(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            # form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()               # 회원가입, 로그인 별개 진행
            user = form.save()          # 회원가입 후 자동 로그인
            auth_login(request, user)   # 회원가입 후 자동 로그인
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def signout(request): # 요청하는 유저 정보가 request에 들어있음
    request.user.delete()
    auth_logout(request) # 탈퇴 후 session 데이터 삭제
    return redirect('accounts:index')

@login_required
def update(request):
    if request.method == 'POST':
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def update_password(request, user_pk):
    if request.method == 'POST':
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # form.save() # 세션 무효화 미적용
            user = form.save() # 세션 무효화 방지 (선택사항)
            update_session_auth_hash(request, user) # 세션 무효화 방지 (선택사항)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user) # 첫 번째 필수 위치 인자가 user
    context = {
        'form': form,
    }
    return render(request, 'accounts/update_password.html', context)