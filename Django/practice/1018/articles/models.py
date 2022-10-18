from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 글 지워지면 댓글도 지워지는 것

    # 1. 대상의 모델(누구 참조할껀데?) 
    # 2. 삭제 시(참조 사라지면 어떻게 할껀데?)