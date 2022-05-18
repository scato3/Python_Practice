N = int(input())

for _ in range(N):
    n = int(input())
    h = 0
    p = 0
    for _ in range(n):
        c, g = map(str, input().split())
        h += int(c)
        p += float(c) * float(g)
    p = round(p / h, 1)
    print(h, p)