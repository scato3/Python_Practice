t = int(input())

for _ in range(t):
    a, b, c = list(map(int, input().split()))

    if a + c > 2 * b:
        if (a + c) % (2 * b) == 0:
            print('YES')
        else:
            print('NO')
    else:
        if (2 * b - a) % c == 0 or (2 * b - c) % a == 0:
            print('YES')
        else:
            print('NO')