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

@csrf_exempt
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == "POST":
        # password와 confirm에 입력된 값이 같다면
        if request.POST["password"] == request.POST["confirm"]:
            # user 객체를 새로 생성
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password"]
            )
            # 로그인 한다
            # auth.login(request, user)
            return redirect("/")
        else:
            return render(request, "failed.html")

    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, "login/signup.html")


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
        response = laftel.sync.searchAnime("나루토")
        # response = laftel.sync.getAnimeInfo(avg_rating)
        
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
    
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnimeInfoSerializer

class AnimeInfoAPIView(APIView):
    def get(self, request):
        try:
            # 이전 코드의 내용을 가져와서 시리얼라이즈
            response = laftel.sync.searchAnime("이로하")
            # result_list = []
            sorted_response = sorted(response, key=lambda item: item.get_data().avg_rating, reverse=True)
            first_info = sorted_response[0]
            anime_info = first_info.get_data()
           
            
            data = {
                "id": anime_info.id,
                "name": anime_info.name,
                "url": anime_info.url,
                "image": anime_info.image,
                "avg_rating": anime_info.avg_rating,
                "content" : anime_info.content,
                "air_time" : anime_info.air_time,
            }

            serializer = AnimeInfoSerializer(data)
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": f"API request error: {str(e)}"}, status=500)
    

from django.http import HttpResponse
import boto3

def list_kinesis_streams(request):
    kvs_client = boto3.client('kinesisvideo', region_name='ap-northeast-2')

    response = kvs_client.list_streams()
    streams = response['StreamInfoList']

    stream_list = []
    for stream in streams:
        stream_list.append(f"Stream Name: {stream['StreamName']}, ARN: {stream['StreamARN']}")

    return HttpResponse("<br>".join(stream_list))

def streaming_view(request):
    kvs_client = boto3.client('kinesisvideo', region_name='ap-northeast-2')

    # 스트림 ARN
    stream_arn = " arn:aws:kinesisvideo:ap-northeast-2:170228352742:stream/streaming-project/1697763444995"

    # 스트리밍 URL 생성
    response = kvs_client.get_data_endpoint(StreamName='streaming-project', APIName='GET_MEDIA')
    streaming_url = response['DataEndpoint']

    return render(request, 'player/play.html', {'streaming_url': streaming_url})
