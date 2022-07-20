n, k = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))
ans = 0
for i in money[::-1]:
    cnt = 0
    if i <= k:
        cnt = k // i
        k -= cnt * i
        ans += cnt
print(ans)