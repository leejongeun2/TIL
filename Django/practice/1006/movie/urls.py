from django.urls import path 
from . import views

app_name = 'movie'

urlpatterns = [
  # http://127.0.0.1:8000/movie/
  path('', views.index, name='index'),
  path('create/', views.create, name='create')
]