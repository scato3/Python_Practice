n = int(input())

for _ in range(n):
    price = float(input())
    print('$%.2lf' % round(price*0.8, 2))