n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in arr:
    ans = 1
    for k in arr:
        if i[0] < k[0] and i[1] < k[1]:
            ans += 1
    print(ans,end=' ')