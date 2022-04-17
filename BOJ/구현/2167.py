N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    sum = 0
    i, j, x, y = map(int, input().split())
    for a in range(i-1, x):
        for b in range(j-1, y):
            sum += board[a][b]
    print(sum)