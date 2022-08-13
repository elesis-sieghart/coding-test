valOrQuestion = lambda x, y: x if x==y else '?'

num = int(input())

origin = input()
wordLen = len(origin)
# 파일 이름의 길이는 모두 같다.
arr = [input() for _ in range(num-1)]

for j in range(num-1):
    tmp = ''
    for i in range(wordLen):
        tmp += valOrQuestion(origin[i], arr[j][i])
    origin=tmp
print(origin)