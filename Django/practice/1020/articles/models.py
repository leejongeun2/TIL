from django.db import models
from django.conf import settings
# pip install Pillow
# pip install django-imagekit
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = '')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # ㄴuser.article_set.all()역참조 경우, user, users중 어떤걸 가져다줘야하는지?오류가 뜸 => 그래서 relative_name을 반드시해야함(같은 모델을 참조하는 상황) 
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = '')
    