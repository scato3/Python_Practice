n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1
cnt = 1

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
        
turn_time = 0

while True:
    turn_left()
    nx = r + dx[d]
    ny = c + dy[d]
    
    if board[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt += 1
        r, c = nx, ny
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if board[nx][ny] == 0:
            r, c = nx, ny
        else:
            break
        turn_time = 0

print(cnt)