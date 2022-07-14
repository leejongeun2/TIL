word = 'banana'
list = []


for char in word :
    list.append(int(ord(char))-32)

print(''.join(map(chr, list)))