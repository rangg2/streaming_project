from django.db import models
import json

# Create your models here.
class anime_info(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    content =models.CharField(max_length=100)
    ended = models.BooleanField()
    awards = models.CharField(max_length=200)
    content_rating = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to='images/', null=True, default='')

    def __str__(self):
        return self.title
    
    def set_awards(self, x):
        self.awards = json.dumps(x)
    
    def get_awards(self):
        return json.loads(self.awards)