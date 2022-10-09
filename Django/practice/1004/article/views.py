from django.shortcuts import render, redirect
from article.models import Article
from .forms import ArticleForm
# from <경로> import <객체>
# Create your views here.

def index(request):
    # 게시글 가져와서
    articles = Article.objects.order_by('-pk')

    # 템플릿에 전달하기
    context = {
        'articles' : articles
    }

    return render(request, 'article/index.html', context) # 사용자는 url로 요청을 보내고, 요청이 서버에 들어오게 되고 url에 있는 함수를 보고 함수 실행
    # 함수에 있는 템플릿을 응답해줌


# 1.게시글 생성 
# > 사용자에게 html form 제공(new), 입력한 데이터를 처리(create)
# 2.url에 입력값이 노출되지 않도록 하려면? => POST => 

# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }

#     return render(request, 'article/new.html', context=context)

def create(request): # 요청정보는 넘어온 정보
    if request.method == 'POST': # 리퀘스트 메서드가 포스트이면 디비에 저장하는 작업을 하고
    # db에 저장하는 로직
    # title = request.POST.get('title') # new에서 입력 받아 넘어온 정보(GET/post)에서 get 꺼냄
    # content = request.POST.get('content')
    # Article.objects.create(title=title, content=content) # 모델에 저장(title컬럼은 title변수 할당,  content컬럼은 content변수 할당)
    
        article_form = ArticleForm(request.POST) # 입력 받을 것이 많다면 많이 써야 되는데, 아티클 폼으로 대체 가능, 폼에다가 사용자 정보를 집어 넣는다.
        if article_form.is_valid(): #아티클 폼이 유효하다면?
            article_form.save() #아티클 폼 저장
            return redirect('article:index') # 앱네임 아티클 인덱스페이지로 이동
        
    else: # 리퀘스트 메서드가 포스트 아닌 경우
        article_form = ArticleForm()
    context = { # 사용자 인풋을 받아서, 검증까지 해서 에러메시지를 만든 아티클폼
    'article_form': article_form
    }
    # 컨텍스트 객체가 입력값을 가지고 있어서 다시 돌아올 수 있도록

    return render(request, 'article/new.html', context=context)
    # 유효하지 않을 때 웹사이트들은 인풋에 빨간색으로 메세지 추가하여 보여줌


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'article/detail.html', context)


def update(request, pk): 
    article = Article.objects.get(pk=pk) # 정보 가져오기
    if request.method == 'POST':
        # post: 인풋값 가져와서 검증하고 디비에 저장
        article_form = ArticleForm(request.POST, instance=article) # 뒤에 있는 내용을 앞에것으로 바꾼다, 기존에 있는 인스턴스를 수정하는 것
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고 상세보기 페이지로가기
            article_form.save()
            return redirect('article:detail', article.pk)
        # 유효성 검사 통과하지 않으면 context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
         # 디비에 저장 된 글 가져와서
        article_form = ArticleForm(instance=article) # 인스턴스를 정함(아티클에 있는 것 그대로 쓰겠다), 여기서 아티클폼: 기존의 인스턴스의 값을 가진 상태의
    context = {
        'article_form': article_form
    }
    return render(request, 'article/update.html', context)

    