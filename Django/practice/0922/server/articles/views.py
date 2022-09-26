from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    names = ['주세환', '오진수', '임수경', '조병진', '촤화영', '이종은']
    name = random.choice(names)
    context = {
        'name': name,
        'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }
    return render(request, 'index.html', context)

def welcome(request, name):
    # 사람들이 /welcome/본인이름을 입력하면, 환영 인사와 이름을 동시에 보여준다. 
    # print(name)

    context = {
        'name' : name,
        'greetings' : ['안녕하세요', 'hello', 'gutentag', 'bonjour'
        ],

        'images' : [
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg'
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_5563F1F93076C8DB0195F78A9B7510DC.jpg'
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_2DB9A10C1F763F7C4C1511959AFD2AFF.jpg'

        ],
    }

    return render(request, 'welcome.html', context)

def menu(request):
    # 새로고침할때마다 랜덤으로 메뉴를 보여준다. 

    menus = ['피자', '김밥', '떡볶이', '메밀소바', '샐러드']
    
    num = random.randrange(0, 5)

    images = ['https://cdn.dominos.co.kr/admin/upload/goods/20220607_tBbZjE5M.jpg?RS=350x350&SP=1',
    'https://upload.wikimedia.org/wikipedia/commons/0/0e/Gimbap_%28pixabay%29.jpg',
    'http://img4.tmon.kr/cdn3/deals/2021/07/15/4500036162/original_4500036162_front_f8dfd_1626343427production.jpg',
    'http://th2.tmon.kr/thumbs/image/ca2/57d/7c0/d048e7ed1_700x700_95_FIT.jpg',
    'https://recipe1.ezmember.co.kr/cache/recipe/2020/01/08/915d7c6597ecfb3960119b7a707171ed1.jpg',

    ]

    context = {
        'menu' : menus[num],
        'images' : images[num],
    }
    
    return render(request, 'menu.html', context)

    

def lotto(request):

    context = {
        'lotto' : []
        
    }

    

    for i in range(5):
        num = random.sample(range(1,46),6)
        context['lotto'].append(num)
        

    
    return render(request, 'lotto.html', context)
    
 


