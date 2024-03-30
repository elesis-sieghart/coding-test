"""
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E) = V+E = V+4V = 5V = 5*m*n = 5*500*500 (m, n의 최대값)
- V : m*n (가로*세로) = 250000
- E : V*4 (좌측맨위는 엣지 2개, 중앙은 엣지 4개, 넉넉잡아 엣지는 4개로 본다) = 100만 < 2억 (1초에 연산 1억, 2초니 2억개)
=> 시간복잡도가 5V(250000*5=125만)이니 2초 2억보다 적아 해당 알고리즘 사용가능.
-*+
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""
from collections import deque

# 두 줄은 입출력 큰경우 잡는 시간을 줄인다. 습관화.
import sys
input = sys.stdin.readline 

# 기본적인 자료구조 생성
n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

# 외워도 무방, (x,y)좌표로 (1,0),(0,1),(-1,0),(0,-1)의 우로부터 반시계.
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m: # 지도밖을 안넘어가도록
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

# 이중for: 보통 y를 먼저돌고 x를 돈다.
cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            # 재방문 방지
            chk[j][i] = True
            # 전체 그림 갯수를 +1
            cnt += 1
            # BFS > 그림 크기를 구해주고 최대값 갱신
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)
