t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    test = [0] * 4

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                if (i + j) % 2 == 0:
                    test[0] += 1
                else:
                    test[1] += 1
            elif arr[i][j] == '.':
                if (i + j) % 2 == 0:
                    test[2] += 1
                else:
                    test[3] += 1

    if (test[0] and test[1]) or (test[2] and test[3]) or (test[0] and test[2]) or (test[1] and test[3]):
        print('#{} {}'.format(tc, 'impossible'))
    else:
        print('#{} {}'.format(tc, 'possible'))