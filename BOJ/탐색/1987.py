dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(input())
    
def bfs(x, y):
    q = set([(x, y, graph[x][y])])
    res = 1
    
    while q:
        x, y, visited = q.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] not in visited:
                    next_visited = graph[nx][ny] + visited
                    q.add((nx, ny, next_visited))
                    res = max(res, len(next_visited))
    return res
    
print(bfs(0, 0))