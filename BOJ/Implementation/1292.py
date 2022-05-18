n, m = map(int, input().split())

ans = []
for i in range(1, m+1):
    for _ in range(i):
        ans.append(i)

print(sum(ans[n-1:m]))