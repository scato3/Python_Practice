from collections import deque

n = int(input())

graph = []
maxNum = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

def bfs(x, y, value):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

result = 0

for i in range(maxNum):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1
    if result < cnt:
        result = cnt

print(result)