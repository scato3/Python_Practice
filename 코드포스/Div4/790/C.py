t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(input())
    
    arr = []
    for i in range(n):
        for j in range(i+1, n):
            sum = 0
            for k in range(m):
                sum += abs((ord(graph[i][k])) - (ord(graph[j][k])))
        
            arr.append(sum)
    print(min(arr))
    