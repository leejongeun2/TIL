from django.shortcuts import render, redirect
from .models import Article, Comment
from articles.forms import ArticleForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False) # 아티클 객체를 받아서
            # 로그인한 유저가 작성자(이티클의 유저)임!
            article.user = request.user 
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form':article_form # 사용자 인풋을 다 받아서, 검증까지 해서 에러메세지를 저장한 article_form(+ 템플릿 내 부트스트랩 폼에 사용)
    } # post일때는 post의 articleform이 context에 들어가고, get일때(해당 패이지 접속)일때는 else의 articleform이 들어감
    # 따라서, 유효한 값이 아닐 때는 post를 받아서, 요청받은 article form!!
    return render(request, 'articles/form.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article) #  movie = Movie.objects.get(pk=pk)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, '글 수정 완료!')
            return redirect('articles:detail', article.pk)
    else:
        article_form  = ArticleForm(instance=article) 

    context = {
        'article_form' : article_form 
        }
    return render(request, 'articles/form.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    context = {
        'article':article
    }
    return render(request, 'articles/index.html', context)

@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article # 게시글은 입력 받은 댓글의 게시글
        comment.user = request.user # 로그인한 유저가 댓글작성자(커멘트의 유저)임!
        comment.save()
    return redirect('articles:detail', article.pk)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    
@login_required
def like(request, pk):
    
    article = Article.objects.get(pk=pk)
    # 만약에 로그인한 유저가 이 글을 좋아요 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():사용 가능
    if request.user in article.like_users.all():
    # 좋아요 삭제하고 
        article.like_users.remove(request.user)
    else:
    # 좋아요 추가하고
        article.like_users.add(request.user)
    # 상세페이지로 리다이렉트
    return redirect('articles:detail', pk)