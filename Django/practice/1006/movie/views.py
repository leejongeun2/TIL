from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from movie.forms import MovieForm
from .models import Movie


# Create your views here.

def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies
    }
    return render(request, 'movie/index.html', context)

@login_required
def create(request):
    # 실제 db에 저장하는 로직
    if request.user.is_authenticated: # 로그인해야지 글작성할 수 있지만 주소에 create입력하면 넘어감, 그럴수 없도록(create주소를 입력해도 넘어가지 않도록) 서버에서 막아주는 것
        if request.method == 'POST':

            movie_form = MovieForm(request.POST) # 사용자가 작성한 내용
            if movie_form.is_valid():
                movie_form.save()
                return redirect('movie:index')
        else:
            movie_form = MovieForm() # 틀만 제공
        context = {
            'movie_form': movie_form
        }
        return render(request, 'movie/new.html', context)
    else: 
        return redirect('accounts:login')
        # 여러 해결책이 있음 1.접근 잘못했다는 페이지 렌더 2.리턴 리다이렉트 로그인페이지


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movie/detail.html', context)



@login_required # 로그인이 필요해! /http://localhost:8000/accounts/login/?next=/movie/1/update/(겟 요청)와 login url이 다른이유는? => 어카운트 뷰에서 안쓰기 때문
# 위 데코레이터는 로그인을 사용자가 요구 되는상황에 있어서 실제로 로그인 페이지로 보내주고 그 이후의 행동을 뷰 함수의 추가적인 처리로써 해결 할 수 있음 
def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie) #  movie = Movie.objects.get(pk=pk)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movie:detail', movie.pk)
    else:
        movie_form  = MovieForm(instance=movie)

    context = {
        'movie_form' : movie_form
        }
    return render(request, 'movie/update.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie:index')
    context = {
        'movie':movie
    }
    return render(request, 'movie/index.html', context)


