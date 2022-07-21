import sys
sys.stdin = open("input1989.txt", "r")

t = int(input())

for tc in range(1, t + 1) :
    data = input()
    temp = ''
    for i in range(len(data)-1, -1, -1) :
        temp += data[i]

    if data == temp :
        print('#%d %d' % (tc, 1))
    else :
        print('#%d %d' % (tc, 0))
