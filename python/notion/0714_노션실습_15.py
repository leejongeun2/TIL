#문자의 위치구하기(a가 처음으로 등장하는 위치)
#문자 순회가 아니라, 인덱스로 접근해서 쓰자 
#원하는 숫자? 
#원하는 방법은 range(len)
word = 'banana'
n = 0
for i in word:
    if i == 'a': 
        print(n) #i가 a일 때, 출력
        break # 그때 멈추고 
    n += 1 #n의 값이 하나씩 커짐
else :
    print(int(-1))

#15-2
#기록을 해야 되서, 리스트 어펜딩
#
word = 'happyhacking'
n = 0
for i in word:
    if i == 'a': #i가 a일떄, 출력
        print(n, end=' ') #멈추는 것 없이 그때 n의 값 출력, 줄바꿈이 자동으로 되버려서 
    n += 1 #n의 값이 하나씩 커짐
