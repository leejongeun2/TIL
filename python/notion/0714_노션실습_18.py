#> 문자열 word가 주어질 때, `**Dictionary**`를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = 'banana'
cnt = {}
for char in word:
    if char in cnt:
        cnt[char] += 1 
    else:
        cnt[char] = 1

for key, value in cnt.items(): #주어진 사전의 키, 값 튜플 쌍의 목록을 표시하는 보기 개체
    print(key, value)