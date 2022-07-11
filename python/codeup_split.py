a = '1 2 3'
# ['1', '2', '3']
# 문자열을 특정 단위로 쪼개줌!
# 리스트!
print(a.split())
numbers = a.split()
result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
print(result)

a = '10:20'
numbers = a.split(':')
print(numbers)
# 출력할 때 sep을 작성하면 값 사이에 들어감
print(numbers[0], numbers[1], sep='^')