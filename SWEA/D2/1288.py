T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * 10
    i = 0
    while True:
        if 0 not in arr:
            break
        else:
            i += 1
            num = str(N * i)
            for j in range(len(num)):
                arr[int(num[j])] = 1
    print('#{} {}'.format(tc, num))
        