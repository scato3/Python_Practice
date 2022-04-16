n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3)%4
        
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                flag = 1 # 들렀다.
                break
    if flag == 0: # 4바퀴 돌았는데 청소할 곳이 없다면
        if board[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r - dx[d], c - dy[d]