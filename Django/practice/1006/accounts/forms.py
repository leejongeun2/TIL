from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
from django.contrib.auth import get_user_model 

class CustomUserCreationform(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ("username", )
# get함수를 호출해라, 직접 참조하지 않도록

class CustomUserChangeForm(UserChangeForm):
# 아티클 c/u에는 아티클폼을 같이 썼는데 user c/u에는 폼을 다르게 쓰는 것은, 사용자는 비밀번호가 다르기 때문
# user c는 비밀번호 두개를 받아서 일치하는 로직이 포함 된 감사한 친구:usercreationform
# user u는 비밀번호 두개를 받을 필요가 없음. 구성 자체가 다르고, 비밀번호는 그대로 입력해서 주면 될꺼같음
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
