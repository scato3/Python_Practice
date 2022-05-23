n, m = map(int, input().split())
arr = {}
for _ in range(n):
    a, b = input().split()
    arr[a] = b

for _ in range(m):
    print(arr[input()])
