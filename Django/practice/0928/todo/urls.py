from django.urls import path
from . import views

# url namesapce => 유얄엘을 이름으로 분류하는 기능
# => 다른 앱에서도 인덱스라는 이름을 사용하기 위한 것

app_name = "todo"

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('delete/<int:todo_pk>', views.delete, name='delete'),
  path('update/<int:todo_pk>', views.update, name='update'),
]
# 해당 주소로 요청하면 뷰의 인덱스 함수 응답, 유알엘 이름을 인덱스로 지정