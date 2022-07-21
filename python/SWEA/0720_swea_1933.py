a = int(input())
for i in range(a): #range(a)를 이용해 a-1회 반복
    if a%(i+1)==0: #i가 0부터 시작하기 때문에 i+1~n까지를 나눌 수 있게 해주고, 나누었을 때 나머지가 0이면 출력
        print(i+1,end=" ")