i = 1
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    ans = (c // b) * a + min(c % b, a)

    print('Case {}: {}'.format(i, ans))
    i += 1