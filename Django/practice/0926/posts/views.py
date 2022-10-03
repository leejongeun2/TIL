from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.



# 첫번째 리드: 글에 데이터목록을 출력
def index(request):
    # 모든 글 목록 보여준다
    # 1. 디비에서 모든 글 불러온다
    posts = Post.objects.all()
    # 2. 템플릿에 보내준다. 
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)

# 두번째 리드: 하나의 데이터에 대한 정보를 출력
# 1. 클릭할 것에 a태그 링크를 걸어줌, 삭제를 할 때 처럼 내가 클릭한 글의 pk값을 동적인자로 전달해야함
# 2. url만들기
# 3. pk값을 이동시키면서 뷰에서 가져오고, 템플릿에서 출력(유알엘 > 뷰 > 템플릿)
def detail(request, pk_):
    # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다. 패쓰와 동일해야함
    # 불러온 데이터를 변수에 할당
    post = Post.objects.get(pk = pk_)

    context = {
        'post' : post,
    }
   # 템플릿에서 변수를 사용하기 위해 컨텍스트를 넣어줌
    return render(request, 'posts/detail.html', context)

def new(request):
    return render(request, 'posts/new.html')


def edit(request, pk_):
    # get메소드를 사용해서 특정 pk데이터를 불러온다. 
    post = Post.objects.get(pk = pk_)
    context = {
        "post" : post,

    }
    return render(request, 'posts/edit.html', context)


def create(request):
    
    # 1. 파라미터로 날라온 데이터를 받아서 

    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. 디비에 저장

    Post.objects.create(title=title, content=content)
    context = {
        'title' : title,
        'content' : content,
    }

    return redirect('posts:index')


# read+ create + 알파
# read : 수정페이지의 디테일을 출력
def update(request, pk_):
    # 업데이트 할 특정 데이터를 불러온다. => pk_를 사용해서

    post = Post.objects.get(pk = pk_)
    # create처럼 데이터를 받아와야함

    title_ = request.GET.get('title')
    content_ = request.GET.get('content')

    # 데이터 수정
    # 내가 불러온 것을 입력 받은 것으로 바꿈
    post.title = title_
    post.content = content_

    post.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect('posts:detail', post.pk) # 인덱스의 첫번째 유알엘과 똑같



def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect('posts:index')

# 1.사용자가 수정하려면 수정 페이지가 있어야함
# 2.수정버튼 누르면 변경사항을 반영할 뷰가 필요함
# 3.edit => new, update => create와 비슷



