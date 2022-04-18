from collections import deque

m, n = map(int, input().split())

board = []
queue = deque([])

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 1:
            queue.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1

bfs()
res = 0

for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)