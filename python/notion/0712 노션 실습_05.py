# 평균구하기
# 변수 두개 설정, 한개는 더하는 것, 한개는 세는 것

numbers = [3, 10, 20]

# 값 초기화
k = 0
j = 0
# 반복
for i in numbers:
		k += i
		j += 1
print(k / j)