from django.db import models
import json

# Create your models here.
class anime_info(models.Model):
    name = models.CharField(max_length=100) # 제목
    url = models.CharField(max_length=100) # 링크
    image = models.CharField(max_length=100) # 커버 사진
    content =models.CharField(max_length=100) # 줄거리
    ended = models.BooleanField() # 완결 여부
    awards = models.CharField(max_length=200) # 받은 상
    content_rating = models.CharField(max_length=100) # 콘텐츠 등급
    viewable = models.BooleanField(default='1') # 시청 가능 여부 ( 결제 여부? )
    genres = models.CharField(max_length=200, default='') # 장르
    tags = models.CharField(max_length=200,default='') # 태그
    airday = models.CharField(max_length=100, default='') # 방영 요일
    production = models.CharField(max_length=100, default='') # 제작사
    

    def __str__(self):
        return self.title
    
    def set_awards(self, x):
        self.awards = json.dumps(x)
    
    def get_awards(self):
        return json.loads(self.awards)
    
    def set_genres(self, x):
        self.genres = json.dumps(x)
    
    def get_genres(self):
        return json.loads(self.genres)
    
class Anime(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.TextField()
    cropped_img = models.TextField()
    is_adult = models.BooleanField(default=False)
    genres = models.JSONField()
    medium = models.CharField(max_length=255)
    distributed_air_time = models.CharField(max_length=255)
    is_laftel_only = models.BooleanField(default=False)
    is_uncensored = models.BooleanField(default=False)
    is_dubbed = models.BooleanField(default=False)
    is_avod = models.BooleanField(default=False)
    avod_status = models.CharField(max_length=255)
    is_viewing = models.BooleanField(default=True)
    latest_episode_created = models.DateTimeField()
    latest_published_datetime = models.DateTimeField()
    is_episode_existed = models.BooleanField(default=True)
    is_expired = models.BooleanField(default=False)