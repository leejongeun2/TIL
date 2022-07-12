# 최댓값 구하기

# 1.반복
numbers = [-10, -100, -30]
k = numbers[0]
for i in numbers:
    # 2. 만약, k값이 이 i보다 작으면 바꾼다. 
		if k < i :
            # print("왔냐?")
				k = i
print(k)