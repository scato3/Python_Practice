from collections import deque
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        z, x, y = q.popleft()
        
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if graph[nz][nx][ny] == 0:
                    q.append((nz, nx, ny))
                    graph[nz][nx][ny] = graph[z][x][y] + 1
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i, j, k])
                
bfs()
z = 1
res = -1

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            res = max(res, k)

if res == 1:
    print(0)
else:
    print(res - 1)