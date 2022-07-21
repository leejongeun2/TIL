# for 문으로 주어진 문자열을 처음부터 확인하고, 만약 글자가 ‘a’이면 continue로 넘어가고, ‘a’가 아니면 새로운 문자열에 추가한다.
word = input()
a_removed_word = ""

for char in word:
    if char =='a':
        continue
    else:
        a_removed_word += char

print(a_removed_word)