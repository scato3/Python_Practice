t = 10

for tc in range(1, t+1):
    n = int(input())
    data = list(map(int, input().split()))

    for i in range(n):
        max_num = max(data)
        min_num = min(data)

        data[data.index(max_num)] -= 1
        data[data.index(min_num)] += 1

        if max(data) - min(data) < 2:
            break

    print('#{} {}'.format(tc, max(data) - min(data)))

