import sys

while True:
    val = list(map(int, sys.stdin.readline().strip().split()))

    if len(val)==3 and val[0]==0 and val[1]==0 and val[2]==0:
        break
    maxNum = max(val)
    val.remove(maxNum)
    print('right') if val[0]**2 + val[1]**2 == maxNum**2 else print('wrong')