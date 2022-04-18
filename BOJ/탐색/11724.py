from collections import deque

n, m = map(int, input().split())

def bfs(v, edge, visited):
    queue = deque([v])
    visited[v] = 1
    
    while queue:
        q = queue.popleft()
        
        for i in edge[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

edges = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(v)
    
visited = [0] * (n+1)
result = 0

for i in range(1, n+1):
    if not visited[i]:
        result += 1
        bfs(i, edges, visited)
    
print(result)