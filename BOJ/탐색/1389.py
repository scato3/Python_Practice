from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def bfs(x):
    visited = [0] * (n+1)
    q = deque()
    q.append(x)
    visited[x] = 1
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
    return sum(visited)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
res = []

for i in range(1, n+1):
    res.append(bfs(i))
    
print(res.index(min(res)) + 1)