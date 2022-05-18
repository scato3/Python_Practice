board = dict()
check = [[0]*5 for i in range(5)]
for i in range(5):
    a = list(map(int,input().split()))
    for j in range(5):
        board[a[j]] = (i,j)
        
print(board)