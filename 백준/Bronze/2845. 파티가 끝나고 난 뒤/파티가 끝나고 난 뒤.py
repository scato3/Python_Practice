a, b = map(int, input().split())
tmp = a * b

arr = list(map(int, input().split()))

for i in arr:
    print(i - tmp, end=' ')