n, k = map(int, input().split())
female = [0] * 7
male = [0] * 7

for _ in range(n):
    s, y = map(int, input().split())
    if s == 0:
        female[y] += 1
    else:
        male[y] += 1

ans = 0

for i in female:
    if i % k == 0:
        ans += i // k
    else:
        ans += (i // k) + 1

for i in male:
    if i % k == 0:
        ans += i // k
    else:
        ans += (i // k) + 1

print(ans)