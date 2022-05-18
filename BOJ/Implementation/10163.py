board = [[0] * 1001 for _ in range(1001)]

n = int(input())

for k in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            board[i][j] = k

cnt_color = [0] * (n+1)

for i in range(1001):
    for j in range(1001):
        if board[i][j]:
            cnt_color[board[i][j]] += 1
            
for i in range(1, n+1):
    print(cnt_color[i])