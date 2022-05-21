t = int(input())

for _ in range(t):
    n = int(input())
    candy = list(map(int, input().split()))
    if n == 1:
        if candy[0] == 1:
            print('YES')
        else:
            print('NO')
    else:
        candy.sort()
        if candy[-1] - candy[-2] <= 1:
            print('YES')
        else:
            print('NO')