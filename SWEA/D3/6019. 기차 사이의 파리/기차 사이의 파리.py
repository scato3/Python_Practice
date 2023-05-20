t = int(input())

for tc in range(1, t+1):
    d, a, b, f = map(int, input().split())

    tmp = d / (a + b) * f

    print('#{} {:.10f}'.format(tc, tmp))
