from django.urls import path
from . import views

"""
메인(r): 게시글 목록(/posts/) / 게시글 상세
작성(c): 글을 작 성하는 페이지(/posts/new/) / 작성완료
수정(u): 글을 수정하는 페이지 / 수정 완료
삭제(d): 글을 삭제 완료 
"""

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'), 
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    # 어떤 주소로(디테일)로 요청하면 어떤 뷰(디테일) 함수를 응답할까? 
    path('detail/', views.detail, name='detail'),
]