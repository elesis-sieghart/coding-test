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