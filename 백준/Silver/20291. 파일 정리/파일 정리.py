n = int(input())
arr = dict()
for _ in range(n):
    k = input().split('.')[1]
    if k not in arr:
        arr[k] = 1
    else:
        arr[k] += 1

file = sorted(arr.items())

for key, value in file:
    print(key, value)