t = int(input())

for _ in range(t):
    a, b, c, d, e = map(int, input().split())

    dog = d - a
    cat = e - b

    if dog <= 0 and cat <= 0:
        print('YES')
    else:
        if dog > 0:
            c -= dog
        if cat > 0:
            c -= cat

        if c >= 0:
            print('YES')
        else:
            print('NO')