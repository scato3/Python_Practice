n = int(input())

for _ in range(n):
    a = list(map(str, input().split()))
    ans = 0
    
    for i in range(len(a)):
        if i == 0:
            ans += float(a[i])
        elif a[i] == '@':
            ans *= 3
        elif a[i] == '%':
            ans += 5
        elif a[i] == '#':
            ans -= 7
    
    print('%.2lf' % ans)