from itertools import combinations

n , m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chicken, home = [], []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i, j))
        if board[i][j] == 2:
            chicken.append((i, j))

ans = 10000
for i in combinations(chicken, m): #조합 사용
    tmp = 0
    for j in home:
        minVal = 10000
        for k in i:
            distance = abs(j[0] - k[0]) + abs(j[1] - k[1])
            minVal = min(minVal, distance)
        tmp += minVal
    ans = min(ans, tmp)

print(ans)