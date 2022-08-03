import sys
sys.stdin = open("input.txt", "r")

t = int(input()) # 테스트 케이스 갯수 입력 받음

for _ in range(t) : # 테스트 케이스 갯수만큼 반복 10 반복
    tc = int(input()) # 테스트 케이스 숫자 입력 받음
    score = list(map(int, input().split())) # 데이터 입력 받음
    data = [0] * 1001 # 0이 1001개 담겨 있는 데이터 리스트 정의 => 점수가 


    for i in score : # 반복문을 통해 score의 값을 하나씩 확인
        data[i] += 1 # 그 값을 인덱스로 하여 data리스트의 해당 인덱스 값(자리)을 1씩 증가 시킴

    max_value = max(data) # 반복작업을 마치면 data 리스트 내 값들 중 최댓값을 구하고, 
    result = [] # 여러개의 최빈값을 담기 위한 리스트 result 생성
    for i in range(len(data)) : # 반복문을 통해 데이터 리스트의 요소를 하나씩 확인
        if data[i] == max_value : # 데이터 리스트 인덱스 값이 최댓값과 같다면 
            result.append(i) # result리스트에 추가

    print('#%d %d' % (tc, max(result))) # 최빈수가 여러개일 때는 가장 큰점수 출력



