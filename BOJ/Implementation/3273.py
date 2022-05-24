n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr.sort()
left = 0
right = n - 1
cnt = 0

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == k:
        cnt += 1
    if tmp < k:
        left += 1
        continue
    right -= 1
print(cnt)