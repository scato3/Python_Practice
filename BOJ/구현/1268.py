n = int(input())
graph = [] 
visited = [0] * n
for i in range(n):
    graph.append(list(map(int, input().split())))
    visited[i] = [0] * n

for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if graph[j][i] == graph[k][i]:
                visited[j][k] = 1
                visited[k][j] = 1
cnt = []
for i in visited:
    cnt.append(i.count(1))
    
print(cnt.index(max(cnt)) + 1)

