N, M = map(int, input().split())

arr1 = []
arr2 = []
for i in range(N):
    row = input()
    if len(row)>1:
        arr1.extend(row.split())
    else:
        arr1.append(row)

for i in range(N):
    row = input()
    if len(row)>1:
        arr2.extend(row.split())
    else:
        arr2.append(row)
arr1 = list(map(int, arr1))
arr2 = list(map(int, arr2))

result = [0]*len(arr1)
for i in range(len(arr1)):
    result[i] = arr1[i] + arr2[i]

result = list(map(str, result))
for i in range(N):
    print(' '.join(result[M*i:M*i+M]))

# 다른사람들의 풀이 (29056KB 60ms)
import sys; 

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]
# r: row,c: column
s = [[a[r][c] + b[r][c] for c in range(M)] for r in range(N)]
for r in s :
    print(' '.join(str(x) for x in r))
    
# ~ for _ in range(N)
# _ 각각에대해 ~
