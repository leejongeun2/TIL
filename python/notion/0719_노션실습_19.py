# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
num=int(input())
k=10
cnt=1
while k<=num: #왜 while이나면 반복의 기준이 생겨야 하기 떄문에, 와일은 종료조건 때까지, for은 반복가능한 것들이 있을 때 그때 한번끝까지 돌겠다는 것
    # 10으로 계속 나눔
    cnt += 1
    k=10**cnt
print(cnt)

#문제풀이
#1.문자로 형변환: 파이써닉한 방법은 보통 아래 방법으로 진행
#number = 123
#print(len(str(number)))

#2. 123
number =123
result = 0
while number !=0:
    result = result//10
    result +=1
print(result)
