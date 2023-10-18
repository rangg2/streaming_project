from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import CustomLoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


@csrf_exempt
def login(request):
    # 이미 로그인한 경우
    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        form = CustomLoginForm(data=request.POST or None)
        if request.method == "POST":

            # 입력정보가 유효한 경우 각 필드 정보 가져옴
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # 위 정보로 사용자 인증(authenticate사용하여 superuser로 로그인 가능)
                user = authenticate(request, username=username, password=password)

                # 로그인이 성공한 경우
                if user is not None:
                    auth_login(request, user) # 로그인 처리 및 세션에 사용자 정보 저장
                    return redirect('/')  # 리다이렉션
        return render(request, 'login/login.html', {'form': form}) #폼을 템플릿으로 전달

@csrf_exempt
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == "POST":
        auth.logout(request)
        return redirect('/')
    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, "login/login.html")


def main(request):
    return render(request, 'main/main.html')