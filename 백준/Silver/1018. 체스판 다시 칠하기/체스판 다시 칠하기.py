n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(input())
    
ans = []
for i in range(n-7):
    for j in range(m-7):
        w_data = 0
        b_data = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if graph[k][l] == 'W':
                        w_data += 1
                    if graph[k][l] == 'B':
                        b_data += 1
                else:
                    if graph[k][l] =='B':
                        w_data += 1
                    if graph[k][l] =='W':
                        b_data += 1
        ans.append(min(w_data, b_data))
        
print(min(ans))