from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  # http://127.0.0.1:8000/articles/
  path('', views.index, name='index'),
  path('<int:pk>/', views.detail, name='detail'),
  path('create/', views.create, name='create'),
  path('<int:pk>/comments/', views.comment_create, name='comment_create'),
  path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]