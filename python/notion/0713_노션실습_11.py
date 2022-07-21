
def 구구단(): #함수 정의
    for i in range(2, 10): #반목문 사용, 2~9범위 반복
        print(f'{i}단') #f-string사용하여 2~9 넣을 값 순서대로 출력
        for j in range(1, 10): #반목문 1~9범위 반복
            print(f'{i} X {j} = {i*j}') #출력
    

구구단()