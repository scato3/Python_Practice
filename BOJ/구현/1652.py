n = int(input())
graph = []

for _ in range(n):
    graph.append(input() + 'X')
graph.append('X' * (n+1))

w, h = 0, 0
for i in range(n+1):
    w_data, h_data = 0, 0
    for j in range(n+1):
        if graph[i][j] == '.':
            w_data += 1
        elif graph[i][j] == 'X':
            if w_data >= 2:
                w += 1
            w_data = 0
        if graph[j][i] == '.':
            h_data += 1
        elif graph[j][i] == 'X':
            if h_data >= 2:
                h += 1
            h_data = 0

print(w)
print(h)