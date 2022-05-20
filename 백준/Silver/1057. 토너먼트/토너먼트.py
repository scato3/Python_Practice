n, m, k = map(int, input().split())

cnt = 0
while True:
    m -= m // 2
    k -= k // 2
    cnt += 1
    if m == k:
        break

print(cnt)