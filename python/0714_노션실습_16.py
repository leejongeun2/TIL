a = ['a', 'e', 'i', 'o', 'u']
word = 'apple'
count = 0
for char in word:
    if char in a:
        count +=1
#print(count)

word = 'apple'
a = 'a', 'e', 'i', 'o', 'u'
cnt = 0

for i in range(len(word)):
    print(word[i])
    if word[i] in a:
        cnt += 1


