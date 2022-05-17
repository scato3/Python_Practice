s, m = map(int, input().split())
money = s - m
coin = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

for i in coin:
    if s - i < 0:
        continue
    else:
        s = s - i

if s == 0:
    print('No thanks')
else:
    if m == s:
        print('Thanks')
    else:
        print('Impossible')