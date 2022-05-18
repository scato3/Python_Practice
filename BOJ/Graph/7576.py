from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))
    
q = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i, j))

def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

bfs()
res = 0

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        else:
            res = max(res, max(i))

print(res - 1)