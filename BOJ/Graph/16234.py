from collections import deque
import math

n, l, r = map(int, input().split())
graph = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    union = [(x, y)]
    count = graph[x][y]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                        union.append((nx, ny))
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        count += graph[nx][ny]
    for x, y in union:
        graph[x][y] = math.floor(count / len(union))
        
    return len(union)

result = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if bfs(i, j) > 1:
                    flag = 1
                    
    if flag == 0:
        break
    result += 1

print(result)