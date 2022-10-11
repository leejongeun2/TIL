from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
]

# 프로필페이지: /accounts/2/
# 뷰: 디테일
# 템플릿 반환: 사용자정보(유저네임)
