n = int(input())
board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(b, b+10):
        for j in range(a, a+10):
            board[i][j] = 1

cnt = 0

for i in range(100):
    for j in range(100):
        if board[i][j]:
            cnt += 1
            
print(cnt)
