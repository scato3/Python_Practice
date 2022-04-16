from collections import deque

n = int(input())

board = [[0] * n for _ in range(n)]
apple = []

k = int(input())
for _ in range(k):
    input_row, input_col = map(int, input().split())
    apple_row, apple_col = input_row - 1, input_col - 1
    board[apple_row][apple_col] = 1
    apple.append((apple_row, apple_col))
    
l = int(input())

change_snake = []

for _ in range(l):
    dis, direct = input().split()
    dis = int(dis)
    change_snake.append((dis, direct))
    
change = [(-1, 0), (0, 1), (1, 0), (0, -1)]
