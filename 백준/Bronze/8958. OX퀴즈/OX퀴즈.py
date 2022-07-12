n = int(input())

for i in range(n):
    OX = input()
    lst = list(OX)
    tmp = 0
    ans = 0

    for k in lst:
        if k == 'O':
            tmp += 1
            ans += tmp
        else:
            tmp = 0
    print(ans)


