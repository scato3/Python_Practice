arr = [int(input()) for _ in range(10)]
sum = 0

for i in arr:
    sum += i
    if sum > 100:
        if sum - 100 > 100 - (sum - i):
            sum -= i
            break

print(sum)