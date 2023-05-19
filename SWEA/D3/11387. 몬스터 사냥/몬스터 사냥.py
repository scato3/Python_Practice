t = int(input())

for tc in range(1, t+1):
    d, l, n = map(int, input().split())

    res = 0

    for i in range(n):
        tmp = d * (1 + i * l * 0.01)
        res += tmp

    print('#{} {}'.format(tc, int(res)))