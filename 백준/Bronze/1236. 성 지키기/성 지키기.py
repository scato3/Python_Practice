n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
    
a = 0
b = 0

for i in range(n):
    if 'X' not in graph[i]:
        a += 1

for j in range(m):
    if 'X' not in (graph[i][j] for i in range(n)):
        b += 1

print(max(a, b))