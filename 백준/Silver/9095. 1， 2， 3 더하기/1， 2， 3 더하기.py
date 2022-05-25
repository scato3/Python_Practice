def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return dp(n-3) + dp(n-2) + dp(n-1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp(n))