from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    rs =1 
    q = deque()
    q.append((x, y))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<n:
                if graph[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
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