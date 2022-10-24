from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
# 프로젝트 설정 시, 해야 되는 것인데 중간에 했기 때문에 디비를 날려야함