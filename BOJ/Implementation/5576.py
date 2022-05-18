a = [int(input()) for _ in range(10)]
b = [int(input()) for _ in range(10)]

a.sort()
b.sort()
print(sum(a[7:]))
print(sum(b[7:]))