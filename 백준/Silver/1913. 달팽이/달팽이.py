n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
value = 1
dir = 0
x = n // 2
y = n // 2
board[x][y] = value
cnt = 1

while value != n * n:
    if dir == 0:
        for i in range(cnt):
            x -= 1
            value += 1
            board[x][y] = value
            if value == n * n:
                break
        dir = 1
    elif dir == 1:
        for i in range(cnt):
            y += 1
            value += 1
            board[x][y] = value
        dir = 2
        cnt += 1
    elif dir == 2:
        for i in range(cnt):
            x += 1
            value += 1
            board[x][y] = value
        dir = 3
    elif dir == 3:
        for i in range(cnt):
            y -= 1
            value += 1
            board[x][y] = value
        dir = 0
        cnt += 1

for i in board:
    print(*i)

for i in range(n):
    for j in range(n):
        if board[i][j] == k:
            print(i+1, j+1)





