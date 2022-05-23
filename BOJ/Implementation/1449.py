n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left = arr[0]
right = arr[0] + l
cnt = 1

for i in range(n):
    if left <= arr[i] < right:
        continue
    else:
        left = arr[i]
        right = arr[i] + l
        cnt += 1

print(cnt)