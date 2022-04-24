dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())

def bfs(x, y):
    q = set([(0, 0, graph[0][0])])
    res = 1
    
    while q:
        x, y, visited = q.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] not in visited:
                    next_visited = visited + graph[nx][ny]
                    q.add((nx, ny, next_visited))
                    res = max(res, len(next_visited))
    return res
    
graph = []
for _ in range(R):
    graph.append(input())
    
print(bfs(0, 0))