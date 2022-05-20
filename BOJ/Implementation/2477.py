n = int(input())
board = [list(map(int, input().split())) for _ in range(6)]
w = 0
w_idx = 0
h = 0
h_idx = 0

for i in range(6):
    if board[i][0] == 1 or board[i][0] == 2:
        if w < board[i][1]:
            w = board[i][1]
            w_idx = i
    if board[i][0] == 3 or board[i][0] == 4:
        if h < board[i][1]:
            h = board[i][1]
            h_idx = i

W = abs(board[(w_idx - 1) % 6][1] - board[(w_idx + 1) % 6][1])
H = abs(board[(h_idx - 1) % 6][1] - board[(h_idx + 1) % 6][1])

print(((w * h) - (W * H)) *n)