n = input()
nums = [0] * 10
card6 = 0

for i in n:
    if i == '6' or i == '9':
        card6 += 1
    else:
        nums[int(i)] += 1

if card6 % 2 == 0:
    card6 = card6 // 2
else:
    card6 = card6 // 2 + 1

nums[6] = card6

print(max(nums))