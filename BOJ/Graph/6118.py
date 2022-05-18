from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x):
    q = deque()
    q.append(x)
    check[x] = 1
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if check[i] == 0:
                check[i] = check[x] + 1
                q.append(i)

bfs(1)
m = max(check)

print(check.index(m), m - 1, check.count(m))