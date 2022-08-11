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
a = [list(map(int, input().split())) for _ in range(N)]     #[[1, 1, 1], [2, 2, 2], [0, 1, 0]]
b = [list(map(int, input().split())) for _ in range(N)]     #[[3, 3, 3], [4, 4, 4], [5, 5, 100]]
# r: row,c: column
s = [[a[r][c] + b[r][c] for c in range(M)] for r in range(N)]
for r in s :
    print(' '.join(str(x) for x in r))

# lambda: sys.stdin.readline().rstrip()
'''
input(): 파이썬에서 가장 자주 쓰는 입력 함수 
sys.stdin.readline(): 하지만 입력 값을 많이 받을 때는 속도를 위해 해당 입력 함수를 사용하는게 좋다.
=> 파이썬 알고리즘 문제를 풀때, 시간초과 에러가 나오는 경우 해결 방법

기본적으로 readline()은 개행문자(줄 바꿈 문자)를 포함하고 있다. 
문자열 마지막에 개행문자의 공백을 처리하는 함수가 아래와 같다.
* rstrip(): 오른쪽 공백을 삭제
* lstrip(): 왼쪽 공백을 삭제
* strip(): 왼쪽, 오른쪽 공백을 삭제
https://yang-wistory1009.tistory.com/54
'''

# ~ for _ in range(N)
# _ 각각에대해 ~
