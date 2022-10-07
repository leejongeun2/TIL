from django import forms
from .models import Movie

# 선언된 모델에 따른 필드구성
# 모델 폼 로직: 사용자에게 html form을 제공, 입력 받은 데이터를 처리
# 1. form 생성
# 2. 유효성 검사

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'summary', 'running_time', 'content']