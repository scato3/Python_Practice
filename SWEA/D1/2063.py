T = int(input())
nums = list(map(int, input().split()))
nums.sort()

index_number = (T-1) // 2

print("{}".format(nums[index_number]))