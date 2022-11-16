t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    temp = max(a) - max(b)

    if temp < 0:
        print('NO')
        continue
    c = list(map(lambda x: max(0, x - temp), a))
    if b == c:
        print('YES')
    else:
        print('NO')