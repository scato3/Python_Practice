n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())
    
for i in board:
    print(i[::-1])