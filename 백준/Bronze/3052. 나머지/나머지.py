num = [0] * 42

for i in range(10):
    a = int(input())
    tmp = a % 42
    num[tmp] += 1

ans = 0
for i in num:
    if i > 0:
        ans += 1

print(ans)
