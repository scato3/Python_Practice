T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int,input().split())
    price1 = P * W
    price2 = Q
    if W > R:
        price2 += (W - R) * S
    cost = min(price1, price2)
    print('#{} {}'.format(tc, cost))
    