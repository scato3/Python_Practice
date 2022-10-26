n, k = map(int, input().split())

cnt = 0

nums = [1] * (n+1)

for i in range(2, len(nums) + 1):
    for j in range(i, n+1, i):
        if nums[j] == 1:
            nums[j] = 0
            cnt += 1
            if cnt == k:
                print(j)
                break