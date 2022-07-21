import sys
sys.stdin = open("1288_input.txt", "r")

T = int(input())
for i in range(T+1): 

    n = int(input())
    value = int(n)
    date = [0] * 10 # ?
    while True :
        for j in range(len(n)) : 
            data[int(n[j])] += 1 #n의 각 자리수를 하나씩 확인하여 그 값을 인덱스로 하여 date를 증가시킴
        if not data.count(0) : #만약 리스트의 요소들 중 0이 없을 경우 0~9까지 모든 숫자가 최소 한번씩 세어진 것이므로,
            #해당 테스트 케이스 번호와 함께 정수형 n 출력
            print(f'#{i}', int(n))
            break

        n = str(value + int(n))
