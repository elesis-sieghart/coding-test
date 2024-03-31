import sys
from collections import deque

# 자료구조
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip()))for _ in range(n)]

# 방위 반시계 매핑
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# graph의 1인 값만 지나가도록 한다.
# 통과가능한 위치에 이전 통과값 +1 해준다. 
# 지나간 위치값을 q에 담아 다시돌린다.
def bfs(x, y):
    q = deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                
    return graph[n-1][m-1]
    
print(bfs(0, 0))