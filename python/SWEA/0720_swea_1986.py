# 1~n 까지 숫자에서 홀수는 더하고 짝수는 뺏을 때, 최종 누적 된 값

import sys
sys.stdin = open('input1986.txt', 'r')

T = int(input())
for i in range(T): #2를 넣었을 떄 0~1

    N = int(input()) #5를 넣었을 떄 
    result = 0
    for i in range(1, N + 1): #1~5
        if i % 2 == 0:
            result -= i
        else:
            result += i
    print(f'#{i + 1}', result)