n, m = map(int, input().split())

arr = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in a:
    arr.append(i)

for i in b:
    arr.append(i)

arr.sort()

print(*arr)