import sys
# (x, y, w, h) => 현재 위치(x, y) => 사각형 (0, 0) ~ (w, h)
x, y, w, h = map(int, sys.stdin.readline().strip().split())

xMin = 0
if(abs(x-0)-abs(x-w)>0):
    xMin = x-w
else:
    xMin = x-0

yMin = 0
if(abs(y-0)-abs(y-h)>0):
    yMin = y-h
else:
    yMin = y-0
print(min(abs(xMin), abs(yMin)))

# 다른 풀이 (29284KB 52ms)
x, y, w, h = map(int,input().split())
print(min(x, y, w-x, h-y))

# 아이구 바보...ㅠ.ㅠ
# 조건에 1 ≤ x ≤ w-1, 1 ≤ y ≤ h-1 봤었다면!!! 
