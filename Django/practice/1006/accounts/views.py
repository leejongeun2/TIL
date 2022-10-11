from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationform
from django.contrib.auth import get_user_model
# Create your views here.

def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:index')

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
