from django.urls import path 
from . import views

app_name = 'movie'

# 기본이 get임

urlpatterns = [
  # http://127.0.0.1:8000/movie/
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/update/', views.update, name='update'),
  path('<int:pk>/delete/', views.delete, name='delete'),
]