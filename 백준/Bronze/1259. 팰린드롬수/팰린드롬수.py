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
