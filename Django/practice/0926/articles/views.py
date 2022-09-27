from django.shortcuts import render
from .models import Article


# Create your views here.

guestbook = []

def index(request):
    # db에서 가져오기
    guestbook = Article.objects.all()
    # select * from articles;
    return render(request, 'articles/index.html', {'guestbook': guestbook})

def create(request):
    content = request.GET.get('content')
    # guestbook.append(content)
    # db에 저장
    # 아티클 디비에서 레코드 만들기
    Article.objects.create(content=content)
    return render(request, 'articles/create.html', {'content': content})