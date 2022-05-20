from collections import deque

graph = [[0] * 101 for _ in range(101)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            graph[i][j] = 1

res = 0
for i in range(1, 101):
    for j in range(1, 101):
        if graph[i][j] == 1:
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if graph[nx][ny] == 1:
                    cnt += 1
            if cnt == 3:
                res += 1
            if cnt == 2:
                res += 2

print(res)

