from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q.append((0, 0))
    cnt = 0
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((ny, nx))
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    cheese.append(cnt)
    return cnt


cheese = []
time = 0
while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break

print(time - 1)
print(cheese[-2])