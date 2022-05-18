n = int(input())
arr = list(map(int, input().split()))

res = 0
ans = []

for i in range(1, n):
    if arr[i] > arr[i-1]:
        res += arr[i] - arr[i-1]
        ans.append(res)
    else:
        res = 0
        ans.append(res)
        
print(max(ans))
        