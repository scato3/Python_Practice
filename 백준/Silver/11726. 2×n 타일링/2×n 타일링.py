ans = [0, 1, 2]
for i in range(3, 1001):
    ans.append(ans[i-2] + ans[i-1])

n = int(input())
print(ans[n] % 10007)