n = int(input())
ans = 0
for i in range(n):
    a = input()
    cnt = 0
    for k in range(len(a) - 1):
        if a[k] != a[k+1]:
            tmp = a[k+1:]
            if tmp.count(a[k]) > 0:
                cnt += 1
    if cnt == 0:
        ans += 1

print(ans)
