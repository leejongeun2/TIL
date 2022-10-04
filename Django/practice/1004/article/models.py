from django.db import models

# Create your models here.

'''
게시판 기능
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간(최초 저장시에만 현재날짜 적용)
- 수정시간(저장 될 때마다 현재날짜로 갱신)
'''
# 1. 모델 설계

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)