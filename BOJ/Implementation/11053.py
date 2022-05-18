n = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))

# dp[i]에 넣을 값을 초기화 해주고, 현재 위치보다 이전에 있는 원소 중에서 현재 원소보다 작은지 체크를 한다.
# 이때 더 작다면 dp[i]에 +1 값을 할당해준다.