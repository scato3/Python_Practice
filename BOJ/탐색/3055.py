from collections import deque

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(input()))
    
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
    
q = deque()

def bfs(Dx,Dy):
    while q:
        x, y = q.popleft()
        
        if graph[Dx][Dy] == 'S':
            return visited[Dx][Dy]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx, ny))
    
    return 'KAKTUS'
        
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            q.append((i, j))
        elif graph[i][j] == 'D':
            Dx, Dy = i, j
            
for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            q.append((i, j))
        
print(bfs(Dx, Dy))