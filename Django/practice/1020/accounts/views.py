from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserChangeForm, CustomUserCreationform
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def index(request):
    users = get_user_model().objects.all()
    context = {"users": users}
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationform(request.POST)
        if form.is_valid():
            user = form.save() # 모델폼의 save메서드의 리턴값(유저)은 해당 모델의 인스턴스다!
            auth_login(request, user) # 세션테이블에 값을 넣어주는 로그인 함수 호출
            return redirect('articles:index') # 회원가입하고 후 로그인페이지 하고 싶으면 여기에 인덱스->로그인으로 바꾸면 됨
    else: 
        form = CustomUserCreationform
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # 사용자가 값을 입력 한 것
        if form.is_valid():
            # 모델폼이 아니니까 세이브 없애고 세션에 저장
            # 로그인 함수는 request, user객체를 인자로 받음
            # user객체는 form에서 인증 된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            # http://localhost:8000/accounts/login/?next=/movie/1/update/ # 로그인해야만 글쓰기로 넘어오고 Url로는 못 넘어오게끔 템플 릿에서 설정했지만, url로 들어올 수 있음, 막기 위해선 글쓰기 함수위에 @를 해야하고, if를 걸어놔야 하지만 글작성 누르면 next url 주소로 들어감, 거기서 로그인하면 인덱스로 리다이렉트 되서, 그럴경우 여기서 글작성으로 리다이렉트할 수 있도록 넘겨줘야함, 그럴 경우 업데이트로 넘어갈 수 있도로 조건문
            return redirect(request.GET.get('next') or 'articles:index') # 앞에꺼가 트루면 앞에꺼가 실행되고 앞에꺼가 false면 뒤에꺼 실행
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
    return redirect('articles:index')

@login_required
def detail(request, pk):
    # user = get_user_model().objects.get(pk=pk)
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

@login_required
def update(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('accounts:detail', request.user.pk)
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/update.html', context)
    else:
        messages.warning(request, '해당 계정 사용자만 수정할 수 있습니다.')
        return redirect('accounts:detail', user.pk)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)
@login_required
def follow(request, pk):
    # 팔로우 상태가 아니면, 팔로우를 누르면 추가(add)
    # 프로필에 해당하는 유저를 로그인한 유저가! 다른사람이 팔로잉 했으면 팔로워를 받아야함
    user = get_object_or_404(get_user_model(), pk=pk)
    # user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다.')
        return redirect('accounts:detail', pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user) # 팔로우한 사람이 requeset.user
    # 이미 팔로우 상태이면, 팔로우 취소 버튼을 누르면 삭제(remove)

    return redirect('accounts:detail', pk)