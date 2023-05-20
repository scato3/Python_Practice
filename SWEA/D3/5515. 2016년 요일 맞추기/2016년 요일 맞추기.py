t = int(input())
month = [31, 29, 31, 30 ,31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, t+1):
    m, d = map(int, input().split())
    days = 0

    if m == 1:
        days = d
    else:
        for i in range(m - 1):
            days += month[i]
        days += d

    print('#{} {}'.format(tc, (days + 3) % 7))

