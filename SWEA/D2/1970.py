T = int(input())

for tc in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8
    for i in range(len(money)):
        if N // money[i] != 0:
            change[i] = N // money[i]
            N = N % money[i]
    print('#{}'.format(tc))
    print(*change)