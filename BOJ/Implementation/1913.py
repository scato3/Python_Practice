n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
r = n // 2
c = n // 2
value = 1
board[r][c] = value
dir = 1
idx = 1

while value != n * n:
    if dir == 1:
        for _ in range(idx):
            r -= 1
            value += 1
            board[r][c] = value
            if value == n * n:
                break
        dir = 2
    elif dir == 2:
        for _ in range(idx):
            c += 1
            value += 1
            board[r][c] = value
        dir = 3
        idx += 1
    elif dir == 3:
        for _ in range(idx):
            r += 1
            value += 1
            board[r][c] = value
        dir = 4
    elif dir == 4:
        for _ in range(idx):
            c -= 1
            value += 1
            board[r][c] = value
        dir = 1
        idx += 1

ans = []
for i in range(n):
    for j in range(n):
        print(board[i][j], end=' ')
        if board[i][j] == k:
            ans.append(i+1)
            ans.append(j+1)
    print()

print(*ans)


