from django.shortcuts import render, redirect

from movie.forms import MovieForm
from .models import Movie


# Create your views here.

def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies
    }
    return render(request, 'movie/index.html', context)

def create(request):
    # 실제 db에 저장하는 로직
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

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movie/detail.html', context)



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


