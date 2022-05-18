from collections import deque

n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    graph[x][y] = 0
    q = deque()
    q.append((x, y))
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
    return cnt
area = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            area.append(bfs(i, j))
if len(area) == 0:
    print(len(area))
    print(0)
else:
    print(len(area))
    print(max(area))