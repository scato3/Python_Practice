from collections import deque

t = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy))
    board[sx][sy] = 1
    
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            print(board[ex][ey] - 1)
            return      
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1
            

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    board = [[0] * n for _ in range(n)]
    bfs(sx, sy, ex, ey)