from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
]

# 프로필페이지: /accounts/2/
# 뷰: 디테일
# 템플릿 반환: 사용자정보(유저네임)

# 로그인 기능 -> aticle create / user create와 비슷
# 1. url: GET/accounts/login/ 
# -> 처리(사용자에게 form을 제공) 
# 2. url: POST/accounts/login/요청 들어오면 
# -> 처리(로그인) 로직 처리(사용자인지 확인하고 장고 세션 테이블에 저장), 쿠키주기
# ->(성공) 로그인 완료 되면 게시글 목록 페이지로 리다이렉트
# ->(실패) 로그인 form

# 로그인 행위: 세션 테이블에 무언가 저장, 쿠키 떨궈줌, 그 정보 담겨진건 리퀘스트 객체
# 로그인과 관련 된 폼은 어센틱케이션폼 => 그냥 폼임(모덷 폼 아님)
# 아티클 직접 만든 모델폼, 회원가입은 장고 내부 폼을 활용해서 모델폼, 로그인은 장고가 만든 폼 활용이지만 그냥 폼을 활용한 것임


# 10/13(목)-회원정보 수정
# 1. url: accounts/<int:Pk>/update/ 회원정보 수정을 하는데 유저별로 할 필요가 없음
# => 로그인한 유저의 정보를 수정하면 됨
# url : /accounts/update 사용하되, 로그인한 사용자에 한해, 로그인한 사용자의 아이디값을 받아서 처리
# GET 요청: form
# post 요청: 실제 수정작업 => 작업 후 개인 프로필페이지로 보내줌(너는 수정한 것을 상세페이지 가서 확인해!)
# 기능(뷰)
# 2. form: 우리는 무슨폼을 주면 될까? => 유저와 연결 된 모델폼 사용하면 됨

# 비밀번호가 바꾸고 로그인 유지하고 싶으면 별도작업 필요 => 수업자료에 나온걸 임포트함
# 탈퇴 하면서 세션 정보 함께 지우고 싶은 경우 = 탈퇴 > 로그아웃 시키면 됨