import sys
import math

def check(val, i):
    if val[i]==val[-(i+1)]:
        return 'ok'
    else:
        return -1

while True:
    val = list(map(int, sys.stdin.readline().rstrip()))
    # val = list(map(int, input()))
    if len(val)==1 and val[0]==0 : break
    result = [check(val, i) for i in range(math.floor(len(val)/2))]

    if -1 in result: print('no')
    else: print('yes')

# 다른 풀이 (29284KB 52ms)
import sys

input=sys.stdin.readline

while 1:
  s=input().rstrip()
  if s=='0': break
  print('yes' if s==s[::-1] else 'no')
# 그냥! 뒤집어서 같으면 되는건데! 
