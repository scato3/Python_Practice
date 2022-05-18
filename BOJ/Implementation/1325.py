from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def bfs(x):
    cnt = 1
    q = deque()
    q.append(x)
    visited = [0] * (n+1)
    visited[x] = 1
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    

result = []
for i in range(1, n+1):
    result.append(bfs(i))
    
ans = max(result)

for i in range(len(result)):
    if ans == result[i]:
        print(i+1, end= ' ')