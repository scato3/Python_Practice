T = int(input())

for tc in range(1, T+1):
    n = list(map(int, input().split()))
    
    h = n[0] + n[2]
    m = n[1] + n[3]
    
    if m > 59:
        h += 1
        m -= 60
    if h > 12:
        h -= 12
    print('#{} {} {}'.format(tc, h, m))