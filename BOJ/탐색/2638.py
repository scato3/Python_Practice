from collections import deque

n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
cnt = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] >= 1:
                        graph[nx][ny] += 1
                    else:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        
while True:
    bfs()
    cht = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                cht = 1
            elif graph[i][j] == 2:
                graph[i][j] = 1
    
    if cht == 1:
        cnt += 1
    else:
        break

print(cnt)