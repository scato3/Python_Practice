from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(str, input())))
    
q = deque()

def bfs(Dx, Dy):
    visited = [[0] * C for _ in range(R)]
    
    while q:
        x, y = q.popleft()
        
        if graph[Dx][Dy] == 'S':
            return visited[Dx][Dy]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx, ny))
    
    return 'KAKTUS'

    
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            q.append((i, j))
        elif graph[i][j] == 'D':
            Dx, Dy = i, j

for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            q.append((i, j))

print((bfs(Dx, Dy)))