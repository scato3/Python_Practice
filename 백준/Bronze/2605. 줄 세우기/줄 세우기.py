n = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.insert(i - arr[i], i+1)

for i in ans:
    print(i,end=' ')