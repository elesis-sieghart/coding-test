from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    rs = 1 
    q = deque()
    q.append((x, y))
    while q:
        ex, ey = q.popleft()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1 and chk[nx][ny] == False:
                    rs += 1
                    chk[nx][ny] = True
                    q.append((nx, ny))
    return rs

cnt = 0
vlist = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            cnt += 1
            vlist.append(bfs(i, j))

print(cnt)
[print(i) for i in sorted(vlist)]
