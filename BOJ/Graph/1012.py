T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                dfs(nx, ny)
        
for _ in range(T):
    M, N, K = map(int, input().split())
    board =[[0] * M for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        m, n = map(int, input().split())
        board[n][m] = 1
        
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)