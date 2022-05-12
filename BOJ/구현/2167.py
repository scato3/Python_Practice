N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

n = int(input())

for _ in range(n):
    sum = 0
    a, b, c, d = map(int, input().split())
    for i in range(a-1, c):
        for j in range(b-1, d):
            sum += graph[i][j]
    print(sum)