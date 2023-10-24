from rest_framework import serializers

class AnimeInfoSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    url = serializers.CharField()
    image = serializers.CharField()
    avg_rating = serializers.FloatField()
    content = serializers.CharField()