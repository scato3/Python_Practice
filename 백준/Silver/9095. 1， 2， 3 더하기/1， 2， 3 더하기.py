def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return dp(n-3) + dp(n-2) + dp(n-1)

n = int(input())
for _ in range(n):
    k = int(input())
    print(dp(k))
