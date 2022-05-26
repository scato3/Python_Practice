arr = [int(input()) for _ in range(9)]
arr.sort()
max = sum(arr)

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if max - arr[i] - arr[j] == 100:
            first, second = arr[i], arr[j]

arr.remove(first)
arr.remove(second)

for i in arr:
    print(i)