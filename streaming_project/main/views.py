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
def tag(request):
    return render(request, 'main/tag.html')
def recommend(request):
    return render(request, 'main/recommend.html')
def daily(request):
    return render(request, 'main/daily.html')
def member(request):
    return render(request, 'main/member.html')
def play(request):
    return render(request, 'player/play.html')

import laftel
from django.http import JsonResponse
from django.http import HttpResponse
import json

def search_anime(request):
    query = "전생슬"
    results = laftel.sync.searchAnime(query)
    # 여기에서 결과를 가공하거나 필요한 데이터를 추출할 수 있습니다.
    return JsonResponse({'results': results})

# def get_anime_info(request, anime_id):
#     anime_info = laftel.sync.getAnimeInfo(anime_id)
#     # 필요한 데이터를 추출하거나 다룰 수 있습니다.
#     return JsonResponse({'anime_info': anime_info})

def laftel_view(request):
    query = "전생슬"
    results = laftel.sync.searchAnime(query)
    context = {'results': results}
    return render(request, 'main/search.html', context)

def get_anime_info(request):
    try:
        # Laftel 라이브러리를 사용하여 "전생슬" 애니메이션 정보를 가져옵니다.
        response = laftel.sync.searchAnime("이로하")
        
        result_list = []
        for item in response:
            result_list.append({
                "id": item.id,
                "name": item.name,
                "url": item.url,
                "image": item.image,
                # 다른 필드도 필요한 만큼 추가
            })

        # JSON으로 직렬화
        json_data = json.dumps(result_list, ensure_ascii=False).encode('utf-8')
        return HttpResponse(json_data, content_type='application/json')

    except Exception as e:
        return HttpResponse(json.dumps({"error": f"API request error: {str(e)}"}), content_type='application/json')