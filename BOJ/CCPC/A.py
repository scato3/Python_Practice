n, m = map(int, input().split())
a, d = map(int, input().split())
s1, s2 = map(int, input().split())

if n % 2 == 1:
    if d == 0:
        if s1 == n:
            print('YES!')
        elif s1 == 1 and s2 > 3:
            print('YES!')
        else:
            print('NO...')
    else:
        if s1 == 1 and s2 < 3:
            print('YES!')
        else:
            print('NO...')

if n % 2 == 0:
    if d == 1:
        if s1 == n:
            print('YES!')
        elif s1 == 1 and s2 > 3:
            print('YES!')
        else:
            print('NO...')
    else:
        if s1 == 1 and s2 < 3:
            print('YES!')
        else:
            print('NO...')
        