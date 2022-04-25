n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
    
m, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))
    
c = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m):
            c[i][j] += a[i][t] * b[t][j]
            
for i in c:
    for j in i:
        print(j, end= ' ')
    print()