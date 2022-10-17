n = int(input())

for _ in range(n):
    a, k = input().split()
    ans = ''
    for i in k:
        ans += int(a) * i
    print(ans)