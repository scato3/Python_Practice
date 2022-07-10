num = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    if i == num:
        cnt += 1

print(cnt)