from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# request.user (로그인 시 유저 객체)
# ==article.user, ==comment.user도 user객체임

class User(AbstractUser):
    # a가 b를 팔로잉 하게 되고 이 것은 서로 친구는 아니다.(symmertrical=false), 사용자에게 필드 추가
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
# 프로젝트 설정 시, 해야 되는 것인데 중간에 했기 때문에 디비를 날려야함