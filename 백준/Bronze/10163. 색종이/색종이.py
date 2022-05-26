n = int(input())
board = [[0] * 1001 for _ in range(1001)]

for k in range(1, n+1):
    a, b, c, d = map(int, input().split())
    for i in range(a, a+c):
        for j in range(b, b+d):
            board[i][j] = k

cnt = [0] * (n+1)

for i in range(1001):
    for j in range(1001):
        cnt[board[i][j]] += 1

for i in range(1, len(cnt)):
    print(cnt[i])