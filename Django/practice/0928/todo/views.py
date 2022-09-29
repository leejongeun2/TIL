from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

# url넣는 곳에 상위경로 잘써줘야함

def index(request):
    todo_ = Todo.objects.all()
    # 우리가 만들어놓은 데이터를 불러오는 코드
    context = {
        "todo" : todo_,
    }
    return render(request, 'todo/index.html', context)


def create(request):
    content = request.GET # 사용자가 보낸 요청을 통으로 가져옴
    print(content['deadline'])

    Todo.objects.create(content=content['content'], priority=content['priority'], deadline=content['deadline'])
    # 통으로 가져온 사용자 정보에서, 컨텐츠 이름으로 된 밸류값을 투두의 컨텐츠 컬럼에 저장
    return redirect('todo:index')



def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk) # todo_pk는 url에서 지정해준 동적인자
    todo.delete()
    
    return redirect('todo:index')


def update(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    if todo.completed == False:
        todo.completed = True
    else:
        todo.completed = False
    
    todo.save()

    return redirect('todo:index')
