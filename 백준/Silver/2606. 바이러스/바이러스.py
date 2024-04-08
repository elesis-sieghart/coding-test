from collections import deque

v = int(input())
e = int(input())

visited = [False for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    # 연결된 컴퓨터의 정보가 언제가 1부터 등장한다는 보장 x
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    deq = deque([x])
    count = 0
    visited[x] = True
    while deq:
        node = deq.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                deq.append(next_node)
                count += 1
    return count

print(bfs(1))
