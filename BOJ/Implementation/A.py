n = int(input())
a, b = map(int, input().split())

cnt = 0

while True:
    if a >= 2:
        a -= 2
        cnt += 1
        n -= 1
    elif b >= 1:
        b -= 1
        cnt += 1
        n -= 1
    else:
        n -= 1
    if n == 0:
        break

print(cnt)