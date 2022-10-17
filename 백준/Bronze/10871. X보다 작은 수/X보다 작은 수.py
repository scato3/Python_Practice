a, b = map(int, input().split())

k = list(map(int, input().split()))

for i in k:
    if i < b:
        print(i, end=' ')