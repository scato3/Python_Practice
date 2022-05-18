n, a = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] < a:
        print(arr[i], end=' ')