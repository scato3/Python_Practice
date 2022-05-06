n, m, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        value = graph[x][y]
        
        for j in range(i+1, n-i): #좌
            x = j
            temp = graph[x][y]
            graph[x][y] = value
            value = temp
        
        for j in range(i+1, m - i):#우
            y = j
            prev = graph[x][y]
            graph[x][y] = value
            value = temp
            
        for j in range(i+1, n - i):#상
            x = n - j - 1
            temp = graph[x][y]
            graph[x][y] = value
            value = temp
        
        for j in range(i+1, m - i):#하
            y = m - j - 1
            temp = graph[x][y]
            graph[x][y] = value
            value = temp

for i in range(n):
    for j in range(m):
        print(graph[i][j], end = ' ')
    print()