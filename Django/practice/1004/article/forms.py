from django import forms
# 장고의 폼가져와
from .models import Article

# 아티클 모델에 있는 모든 필드를 가져와 쓰겠다. 
# 기존 폼 대체 -> 모델폼의 인스턴스를 넘겨줄 것임 -> 컨텍스트
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
