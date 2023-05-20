t = int(input())

for tc in range(1, t+1):
    n = int(input())
    k = round(pow(n, 1/3), 2)

    if int(k) == k:
        print('#{} {}'.format(tc, int(k)))
    else:
        print('#{} {}'.format(tc, -1))
