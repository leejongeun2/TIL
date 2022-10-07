from django.shortcuts import render, redirect

from movie.forms import MovieForm
from .models import Movie

# Create your views here.

def index(request):
    movie = Movie.objects.order_by('-pk')
    context = {
        'movie':movie
    }
    return render(request, 'movie/index.html', context)

def create(request):
    # 실제 db에 저장하는 로직
    if request.method == 'POST':

        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movie:index')
    else:
        movie_form = MovieForm()
    context = {
        'movie_form': movie_form
    }
    return render(request, 'movie/new.html', context)

