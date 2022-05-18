arr = list(map(str, input().split(' ')))
sum = 0
for i in range(len(arr)):
    if len(arr[i]) > 0:
        sum += 1

print(sum)