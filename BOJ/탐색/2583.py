from collections import deque

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    cnt = 1
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    q.append((ny, nx))
                    cnt += 1
    return cnt
            
res = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            res.append(bfs(i, j))
            
res.sort()
print(len(res))
print(*res)