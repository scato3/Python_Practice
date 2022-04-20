from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())

graph = [list(map(str, input())) for _ in range(n)]
    
visited = [[0] * n for _ in range(n)]
cnt1 = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt1 += 1
            

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
            
visited = [[0]* n for _ in range(n)]
cnt2 = 0
            
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt2 += 1
            
print(cnt1, cnt2)