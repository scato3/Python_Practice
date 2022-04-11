T = int(input())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    res = 0
    
    if m1 == m2: # 같은 달이면 일의 차만 구하면 됌
        res = d2 - d1 + 1
    else:
        res = month[m1] - d1 + 1
        for i in range(m1+1, m2):
            res += month[i]
        res += d2
    print('#{} {}'.format(tc, res))
