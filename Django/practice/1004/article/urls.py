from django.urls import path # url설정을 앱 단위로!
# 장고유알엘 파일에서 패쓰를 가져와라! 
from . import views # 현재파일에서 뷰를 가져와라!

app_name = 'article'



urlpatterns = [
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),

    # http://127.0.0.1:8000/articles/new/
    # > 사용자에게 html form 제공(new)
    # path('new/', views.new, name='new'), # 사용자가 new url로 요청을 보내고 new함수 실행, new함수의 템플릿 응답

    # http://127.0.0.1:8000/articles/create/
    # 입력한 데이터를 처리(create)
    path('create/', views.create, name='create'),

    # http://127.0.0.1:8000/articles/1/ : 1번글
    # http://127.0.0.1:8000/articles/3/ : 3번글
    path('<int:pk>/', views.detail, name='detail'),
    
    # http://127.0.0.1:8000/articles/1/update/ : 1번글 수정
    # http://127.0.0.1:8000/articles/3/update/ : 3번글 수정
    path('<int:pk>/update/', views.update, name='update'),

]