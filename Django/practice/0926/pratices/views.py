from multiprocessing import context
from unittest import result
from django.shortcuts import render
import random

# Create your views here.

def number(request, number):

    num=int(number)
    text = 0
    if num==0:
        text='0'
    elif num%2==1:
        text='홀수'
    elif num%2==0:
        text='짝수'
    

    context = {
        'num' : num,
        'text' : text,
    }

    return render(request, 'pratices/is-odd-even.html', context)


def num(request, a, b):
    a = int(a)
    b = int(b)
    result_1 = a + b
    result_2 = a - b
    result_3 = a*b
    result_4 = a//b

    context = { 
        'result_1' : result_1,
        'result_2' : result_2,
        'result_3' : result_3,
        'result_4' : result_4,
        'a' : a,
        'b' : b,
    
    }

    return render(request, 'pratices/calculate.html', context)


def name(request):
    return render(request, 'pratices/name.html')


def answer(request):
    name = request.GET['name']

    animals = ['말', '강아지', '토끼', '호랑이']
    animal = random.choice(animals)

    context = {
        'name' : name,
        'animal' : animal,
    }

    return render(request, 'pratices/answer.html', context)

def lorem_input(request):
    return render(request, 'pratices/lorem_input.html')


def lorem_result(request):
    name1 = int(request.GET['a'])
    name2 = int(request.GET['b'])

    word = ['바나나', '딸기', '사과', '배']
    
    context = {
        'c' : []
        
    }

    for i in range(name1):
        temp = []
        for j in range(name2):
            temp.append(random.choice(word)) 
        context['c'].append(temp)

    return render(request, 'pratices/lorem_result.html', context)






    