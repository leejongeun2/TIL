import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for i in range(1, t + 1):
  a, b = list(map(int, input().split()))
  print('#{} {} {}'.format(i, a // b, a % b)) #몫을 출력, 나머지를 출력 
  #format 함수는 문자열을 출력할 때, 서식지정자를 사용하여 출력하고자 할 때


