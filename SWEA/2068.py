T = int(input())
maxNum = 0
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    maxNum = max(nums)
    print("#{} {}".format(test_case, maxNum))