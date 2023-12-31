from rest_framework import serializers
from .models import Anime

class AnimeInfoSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    url = serializers.CharField()
    image = serializers.CharField()
    avg_rating = serializers.FloatField()
    content = serializers.CharField()
    air_time = serializers.CharField()

class AnimeSerializer(serializers.Serializer):
    class Meta:
        model = Anime
        fields = '__all__'