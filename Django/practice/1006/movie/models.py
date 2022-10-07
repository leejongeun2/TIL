from django.db import models

# Create your models here.

class Movie(models.Model): # Movie모델 클래스는 models에 있는 model을 상속받아서 만듦 => 설계는 했지만 기능 자체는 상속을 받아 사용하고 싶기 때문
    title = models.CharField(max_length=20)
    summary = models.TextField()
    running_time = models.IntegerField()
    content = models.TextField()
