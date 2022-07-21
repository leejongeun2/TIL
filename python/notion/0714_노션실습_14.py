#문자의 갯수 구하기
#'apple', a 카운트
#긱 요소별 체크하면서 바를 정 하나씩 체크하는 모음 변수
# 전체 체크하는 것은 for 문 -> 반복 가능
#word의 요소를 하나씩 char 바인딩
#안녕하세요
word = 'apple'
cnt = 0
for i in word:
    if i == 'a':
        cnt +=1
print(cnt)