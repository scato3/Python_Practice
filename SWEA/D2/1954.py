T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    r,c = 0, 0
    dist = 0
    
    for n in range(1, N * N +1):
        arr[r][c] = n
        r += dx[dist]
        c += dy[dist]
        if r < 0 or c < 0 or r >= N or c >= N or arr[r][c] !=0:
            r -= dx[dist]
            c -= dy[dist]
            dist = (dist + 1) % 4
            r += dx[dist]
            c += dy[dist]
    print('#{}'.format(tc))
    for i in range(arr):
        print(*i)   