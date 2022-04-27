graph = []

for _ in range(9):
    graph.append(list(map(int, input().split())))
    
maxsum = 0
x = 0
y = 0
    
for i in range(9):
    for j in range(9):
        if graph[i][j] > maxsum:
            maxsum = graph[i][j]
            x = i+1
            y = j+1
            
print(maxsum)
print(x, y)

