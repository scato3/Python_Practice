arr = [int(input()) for _ in range(9)]

max_sum = sum(arr)

for i in range(len(arr)):
    for j in range(1, len(arr)):
        if max_sum - arr[i] - arr[j] == 100:
            first, second = arr[i], arr[j]
arr.remove(first)
arr.remove(second)
arr.sort()

for i in range(len(arr)):
    print(arr[i])
            