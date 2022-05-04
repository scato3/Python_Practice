for _ in range(3):
    a = list(map(int, input().split()))
    s = a[5] - a[2]
    m = a[4] - a[1]
    h = a[3] - a[0] 
    
    if s < 0 :
        m -= 1
        s += 60
    if m < 0:
        h -= 1
        m += 60

    print(h, m, s)