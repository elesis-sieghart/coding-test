import sys
# (x, y, w, h) => 현재 위치(x, y) => 사각형 (0, 0) ~ (w, h)
x, y, w, h = map(int, sys.stdin.readline().strip().split())

x_min = 0
if(abs(x-0)-abs(x-w)>0):
    x_min = x-w
else:
    x_min = x-0

y_min = 0
if(abs(y-0)-abs(y-h)>0):
    y_min = y-h
else:
    y_min = y-0
print(min(abs(x_min), abs(y_min)))
