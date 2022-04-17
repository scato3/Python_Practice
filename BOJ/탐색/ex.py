n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))
    
visited = [[0] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = [(0, 0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop()
    
    if x == n - 1 and y == m - 1:
        print(visited[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and board[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))