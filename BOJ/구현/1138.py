n = int(input())
a = list(map(int, input().split()))
b = list()

for i in range(n):
    b.insert(a[n-1-i], n-i)

print(*b)