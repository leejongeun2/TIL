from django.db import models

# genre클래스를 만듬
# models.modes 상속받는 이유: 내가 직접 클래스를 만드는 것이 아니라, 미리 만들어진 기능들을 활용하고 싶어서 
class Genre(models.Model):
    title = models.TextField()

# 마이그레이션 파일을 만들고, 디비에 반영 
# shell 환경에서 테스트를 해볼 수 있음(조작)
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()