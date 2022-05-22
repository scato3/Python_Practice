n, m = map(int, input().split())
graph = [[0] * n for _ in range(m)]
k = int(input())
value = 1
x = m - 1
y = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 0

if n * m < k:
    print(0)
    exit()

while value != k:
    graph[x][y] = value

    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[nx][ny] != 0:
        dir += 1

        if dir == 4:
            dir = 0

        nx = x + dx[dir]
        ny = y + dy[dir]

    x, y, value = nx, ny, value + 1

print(y+1, m - x)

