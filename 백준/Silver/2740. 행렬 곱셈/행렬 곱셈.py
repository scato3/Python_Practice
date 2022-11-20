n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]

b, k = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(b)]

arr3 = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for s in range(m):
            arr3[i][j] += arr1[i][s] * arr2[s][j]

for i in arr3:
    for j in i:
        print(j, end=' ')
    print()

