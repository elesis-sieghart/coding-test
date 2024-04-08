from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y, graph, chk, n, m):
    q = deque()
    q.append((x, y))

    while q:
        ex, ey = q.popleft()
        for i in range(4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == 1 and chk[nx][ny] == False:
                    chk[nx][ny] = True
                    q.append((nx, ny))

def find_cnt(graph, chk, n ,m):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and chk[i][j] == False:
                cnt += 1
                chk[i][j] = True
                bfs(i, j, graph, chk, n, m)
    return cnt

num = int(input())
cnt_list = []
for _ in range(num):
    # 1개의 테스트 케이스에 대한 가로, 세로, 배추위치수
    m, n, k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    chk = [[False]*n for _ in range(m)]

    vlist = [map(int, input().split()) for __ in range(k)]
    for v in vlist:
        ex, ey = v
        graph[ex][ey] = 1    
    
    cnt_list.append(find_cnt(graph, chk, n, m))

[print(cnt) for cnt in cnt_list]

