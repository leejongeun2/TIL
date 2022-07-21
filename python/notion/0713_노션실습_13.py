
# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

import string


word = input()
reversed_str = ''
for i in word:
    reversed_str = i + reversed_str # ename = a + rename 라는 식은 a 에 rename(현재값) 을 더해서 rename(이후값) 새로운 값이 되고
# rename += a 라는 식은
# rename = rename + a 와 같은 식
print(reversed_str)