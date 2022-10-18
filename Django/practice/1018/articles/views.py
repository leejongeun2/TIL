from django.shortcuts import render, redirect
from .models import Article, Comment
from articles.forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)
# 게시글 상세에서 댓글 목록 출력 => 템플릿 => 템플릿에서 쓸 수 있는 변수 context로 넘겨준 친구들
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comments' : article.comment_set.all(),
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form':article_form # 사용자 인풋을 다 받아서, 검증까지 해서 에러메세지를 만든 article_form
    }
    return render(request, 'articles/new.html', context)


def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST) # comment_form은 모델폼의 인스턴스
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # save하기 전 멈추라는 것임, 너가 직접 하지말고 객체를 주면 내가 넣을 값들이 필요해서 그걸 하고 그 다음에 세이브 호출 할께!
        comment.article = article # 리턴한 객체를 내가 조작해서 // # save 후 리턴 받은 comment는 모델의 인스턴스 # 모델폼의 세이브 메서드는 리턴 값이 그 모델의 인스턴스임, 인스턴스 직접 조작
        comment.save() # 커멘트 모델의 아티클 필드는 아티클 받은 객체(위에 오브젝트)와 같다는 것(comment.article = article)을 저장할래, 직접 save 호출 
    return redirect('articles:detail', article.pk)

# comment.article 는 article객체다. 
# article.Comment_set => 커멘트의 쿼리셋(댓글 들)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)