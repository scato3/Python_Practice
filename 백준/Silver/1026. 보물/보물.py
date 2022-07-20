n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
ans = 0
for i in range(n):
    x = a[i]
    y = b.pop(b.index(max(b)))
    ans += x * y

print(ans)
