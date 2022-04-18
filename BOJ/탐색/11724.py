from collections import deque

def bfs(edge, start, visited):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        for i in edge[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
    
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(edges, i, visited)
        cnt += 1

print(cnt)