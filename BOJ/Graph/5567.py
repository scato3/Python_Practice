from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
check = [0] * (n+1)

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

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
bfs(1)
max_sum = 0

for i in check:
    if 2 <= i <= 3:
        max_sum += 1
        
print(max_sum)