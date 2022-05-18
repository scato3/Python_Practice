n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
    
check = min(n, m)
result = 0
for i in range(n):
    for j in range(m):
        for k in range(check):
            if i + k < n and j + k < m and graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k]:
                result = max(result, (k+1) ** 2)

print(result)