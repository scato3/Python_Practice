a = input()
n = len(a)

arr = []
arr2 = []
arr3 = []
for i in range(1, n+1):
    if n % i == 0:
        arr.append((i, n//i))

for r, c in arr[::-1]:
    if r <= c:
        arr2.append(r)
        arr3.append(c)

print(arr)
R = arr2[0]
C = arr3[0]

print(R, C)

graph = [['' for _ in range(C)] for _ in range(R)]

k = 0
for j in range(C):
    for i in range(R):
        graph[i][j] = a[k]
        k += 1

for i in range(R):
    for j in range(C):
        print(graph[i][j], end='')