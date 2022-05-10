from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

n, m, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]

q = deque()

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    q.append([nz, nx, ny])

for i in range(h):
    for j in range(m):
        for k in range(n):
            if graph[i][j][k] == 1:
                q.append([i, j, k])

bfs()
res = 0
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