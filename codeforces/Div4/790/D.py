from re import I, X


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    ans = 0
    for i in range(n):
        for j in range(m):
            xi = i
            yi = j
            sum = 0
            while 0 <= xi < n and 0 <= yi < m:
                sum += graph[xi][yi]
                xi += 1
                yi += 1
            xi = i
            yi = j
            while 0 <= xi < n and 0 <= yi < m:
                sum += graph[xi][yi]
                xi += 1
                yi -= 1
            xi = i
            yi = j
            while 0 <= xi < n and 0 <= yi < m:
                sum += graph[xi][yi]
                xi -= 1
                yi += 1
            xi = i
            yi = j
            while 0 <= xi < n and 0 <= yi < m:
                sum += graph[xi][yi]
                xi -= 1
                yi -= 1
            
            sum -= graph[i][j] * 3
            ans = max(ans, sum)
    print(ans)