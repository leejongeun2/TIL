from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationform
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# 1.버튼을 안만들어 놨는데, url로 직접 접근 가능
# 어디서 막을 것이냐? => view(서버)에서 막아두면 됨
# 2. 어떻게 막냐? => 로그인 여부를 직접 조건문으로 쓸 수 있는데, 
# @login_reqirede데코를 쓸 수 있음 => 역할은 /next=/movie/1/update url로 로그인 페이지로 보내줌
# 3. 사용자가 로그인 html form을 보고 내용을 채우고 ok버튼 누르면
# 4. url이 post의 /next=/movie/1/update고 뷰의 로그인 함수 실행
# => 모델폼에 받아서 유효성 확인하고, 로그인하고, 리다이렉트 한 순간에 위 post url로 정보 보내줌
# redirect 할때, url GET파라미터로 보내준 값을 쓴다. or구문은 앞에값이 트루면 리턴하고 뒤는 검사 안함, 앞에값이 false면 뒤를 리턴

def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationform(request.POST)
        if form.is_valid():
            user = form.save() # 모델폼의 save메서드의 리턴값(유저)은 해당 모델의 인스턴스다!
            auth_login(request, user) # 세션테이블에 값을 넣어주는 로그인 함수 호출
            return redirect('movie:index') # 회원가입하고 후 로그인페이지 하고 싶으면 여기에 인덱스->로그인으로 바꾸면 됨

    else: 
        form = CustomUserCreationform
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    
    #django 쿼리셋 받아보는 메서드
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

# valid까지만 코드 적으면 유효하지 않아서 맨밑에 context가 실행되므로, form을 변경해줘야함
# ==> request.post는 정상이고, 어센틱폼을 수정해야함 => 모델폼이 아니므로, [리퀘스트 내놔! 데이터 키워드 알규멘트로 리퀘스트 포스트가 들어옴]
def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # 사용자가 값을 입력 한 것
        if form.is_valid():
            # 모델폼이 아니니까 세이브 없애고 세션에 저장
            # 로그인 함수는 request, user객체를 인자로 받음
            # user객체는 form에서 인증 된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            # http://localhost:8000/accounts/login/?next=/movie/1/update/
            return redirect(request.GET.get('next') or 'movie:index') # 앞에꺼가 트루면 앞에꺼가 실행되고 앞에꺼가 false면 뒤에꺼 실행
            # if request.GET.get('next'): #== /movie/1/update/ request.GET하면 딕셔너리가 나오고 딕셔너리에 next가 있으면 밸류가 따라옴
            #     return redirect(request.GET.get('next'))
            # else:
            #     return redirect('movie:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)
    
def logout(request):
    auth_logout(request) # 요청에 대한 정보, 디비에 저장 된 세션 정보를 날려버리는 행위
    messages.warning(request, '로그아웃 하였습니다.') # 경고 메세지 노출(빨간색) -> 템플릿에도 반영해야함(베이스에 한번만 반영하면 됨)
    return redirect('movie:index')

@login_required #이걸 해놓으면 프로필 수정 페이지를 로그아웃 한 상태에서 들어올일 없다.(수정페이지를 가도 로그인 페이지로 접속됨), request.user로 유저객체를 쓰는 뷰함수에서는 무조건 쓰는게 좋음(로그인한 정보를 사용해서 뭘 하겠다라는 것이기 때문)
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk) # 여기까지만 쓰면 안되고 pk값을 받아와야하기 떄문에 request.user.pk를 넣어줌
    else:
        form = CustomUserChangeForm(instance=request.user) # 기존값 로그인
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)



  
