n = int(input())
ans = 0
n_len = len(str(n))

for i in range(n_len - 1):
    ans += 9 * 10 ** i * (i + 1)

print(ans + (n - 10 ** (n_len - 1) + 1) * n_len)