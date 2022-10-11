from django.db import models
from django.contrib.auth.models import AbstractUser
# Abstractuser란? => username등 여러 필드가 설정되어있음 
# Abstractuser는 AbstractBaseUser를 상속받고 있음
# AbstractBaseUser는 패스워드, 라스트 로그인등이 있음, 저장할때는 패스워드 관련 설정있음
# AbstractBaseUser는 models.model을 상속 받고 있음
# Create your models here.

# 우리에게 유저 모델은 이미 존재 => auth_user
# admin 등록 시, 이미 해당 모델에 등록
# 직접 정의하는 것이 아니라 내장되어있는 모델을 가져와서 간편하게 활용 => 클래스 상속!!
# 앱이름_모델이름
# 유저 모델 사용하는 방법은? => 커스텀 유저 모델로 대체함
# 기본 유저 모델을 커스텀 유저 모델로 대체해서 사용
# 모델을 직접 정의한 것이 아니라, 장고 내부에 있는 것을 끄집어 내서 migrate함
# 이제 auth_user테이블이 아니라 accounts_user 테이블을 사용하게됨 // acoounts_user 모델에 저장됨
class User(AbstractUser):
    pass