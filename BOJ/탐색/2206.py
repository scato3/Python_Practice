from collections import deque

n, m = map(int, input().split())
graph = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input())))
    
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    visited[x][y][z] = 1
    
    while q:
        x, y, z = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 0: # 벽에 막혀있고 안가봤으면
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    q.append((nx, ny, 1))
                
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1
    
print(bfs(0, 0, 0))