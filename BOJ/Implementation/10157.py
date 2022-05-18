c, r = map(int, input().split())
graph = [[0] * c for _ in range(r)]
k = int(input())
x = r - 1
y = 0
dir = 0
value = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if c * r < k:
    print(0)
    exit()

while value != k:
    graph[x][y] = value
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] != 0:
        dir += 1
        
        if dir == 4:
            dir = 0
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
    x, y, value = nx, ny, value + 1

print(y+1, r - x)
