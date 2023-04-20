n, k = map(int, input().split())
arr = []

for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

arr.sort(key = lambda x:(-x[1],-x[2],-x[3]))

for i in range(n):
    if arr[i][0] == k:
        idx = i

for i in range(n):
    if arr[idx][1:] == arr[i][1:]:
        print(i+1)
        break