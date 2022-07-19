import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for x in range(1, T + 1):
    a, b = map(int, input().split())
    print("#{} {} {}".format(x, a//b,a%b))


