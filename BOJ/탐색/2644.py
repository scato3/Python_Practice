from collections import deque

N = int(input())
a, b = map(int, input().split())

n = int(input())

graph = [[]  for _ in range(N+1)]
ans = [0] * (N+1)

def bfs(x):
    q = deque()
    q.append(x)
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if ans[i] == 0:
                ans[i] = ans[x] + 1
                q.append(i)

for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
bfs(a)

if ans[b] > 0:
    print(ans[b])
else:
    print(-1)