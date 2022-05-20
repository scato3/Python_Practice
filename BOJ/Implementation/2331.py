a, b = map(int, input().split())
nums = [a]

while True:
    num = 0
    for i in str(nums[-1]):
        num += int(i) ** b

    if num in nums:
        break
    else:
        nums.append(num)

print(nums.index(num))