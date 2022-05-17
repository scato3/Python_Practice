n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(input())

cnt = 0
char = ''
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if graph[j][i] == 'A':
            a += 1
        if graph[j][i] == 'C':
            c += 1
        if graph[j][i] == 'G':
            g += 1
        if graph[j][i] == 'T':
            t += 1
    
    if max(a, c, g, t) == a:
        char += 'A'
        cnt += c + g + t
    elif max(a, c, g, t) == c:
        char += 'C'
        cnt += a + g + t
    elif max(a, c, g, t) == g:
        char += 'G'
        cnt += a + c + t
    elif max(a, c, g, t) == t:
        char += 'T'
        cnt += a + c + g
    
print(char)
print(cnt)