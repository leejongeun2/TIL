from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def index(request):
    # 모든 글 목록 보여준다
    # 1. 디비에서 모든 글 불러온다
    posts = Post.objects.all()
    # 2. 템플릿에 보내준다. 
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')


def create(request):
    
    # 1. 파라미터로 날라온 데이터를 받아서 

    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. 디비에 저장

    Post.objects.create(title=title, content=content)
    context = {
        'title' : title,
        'content' : content,
    }

    return redirect('posts:index')


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect('posts:index')

