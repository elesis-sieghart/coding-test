import sys

num = int(input())
arr = [sys.stdin.readline().strip() for _ in range(num)]

origin = arr[0]
wordLen = len(origin)

for j in range(num):
    tmp = ''
    for i in range(wordLen):
        tmp += (lambda x, y: x if x==y else '?')(origin[i], arr[j][i])
    origin = tmp
print(origin)

# 다른 풀이 (동일)
n = int(input())
words = []
for _ in range(n):
    words.append(input())

m = len(words[0])
answer = list(words[0])
for i in range(m):
    for j in range(1, n):
        if answer[i] != words[j][i]:
            answer[i] = '?'
    
print(''.join(answer))
