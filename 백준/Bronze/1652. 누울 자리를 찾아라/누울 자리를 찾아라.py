n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
    
w_data = 0
h_data = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[i][j] == '.' :
            cnt += 1
        
        if graph[i][j] == 'X':
            cnt = 0
        
        if cnt == 2:
            w_data += 1
            
for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[j][i] == '.' :
            cnt += 1
        
        if graph[j][i] == 'X':
            cnt = 0
        
        if cnt == 2:
            h_data += 1

print(w_data, h_data)