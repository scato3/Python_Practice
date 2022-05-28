n = int(input())
arr = []
for _ in range(n):
    a = input()
    arr.append(a)

ans = []
for i in arr:
    if i[::-1] in arr:
        ans.append(i)
        break

print(len(ans[0]), end=' ')
print(ans[0][len(ans[0]) // 2])
