graph = []

for _ in range(9):
    graph.append(list(map(int, input().split())))
    
k = 0
idx = []
for i in range(9):
    for j in range(9):
        if k < graph[i][j]:
            k = graph[i][j]

for i in range(9):
    for j in range(9):
        if k == graph[i][j]:
            print(k)
            print(i+1, j+1)