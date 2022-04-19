from collections import deque
import copy

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
max_result = 0

def virus():
    global max_result
    result = 0
    q = deque()
    temp = copy.deepcopy(graph)
    
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
                
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))
    
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1
    
    max_result = max(max_result, result)
            
                

def wall(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0
                
wall(0)
print(max_result)