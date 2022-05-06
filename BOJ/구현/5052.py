N = int(input())

for _ in range(N):
    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()
    flag = 1
    
    for i in range(n-1):
        length = len(nums[i])
        if nums[i] == nums[i+1][:length]:
            flag = 0
    
    if flag:
        print('YES')
    else:
        print('NO')