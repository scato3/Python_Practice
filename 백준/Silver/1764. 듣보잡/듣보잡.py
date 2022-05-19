n, m = map(int, input().split())
a = set()
for _ in range(n):
    a.add(input())
b = set()
for _ in range(m):
    b.add(input())

res = sorted(list(a & b))

print(len(res))
for i in res:
    print(i)
