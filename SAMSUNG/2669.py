visited = [[0] * 101 for _ in range(101)]

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            visited[i][j] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        cnt += visited[i][j]

print(cnt)