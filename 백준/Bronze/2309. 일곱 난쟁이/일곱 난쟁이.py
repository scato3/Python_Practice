arr = [int(input()) for _ in range(9)]
maxsum = sum(arr)

for i in range(len(arr)):
    for j in range(len(arr)):
        if maxsum - arr[i] - arr[j] == 100:
            a = arr[i]
            b = arr[j]

arr.remove(a)
arr.remove(b)
arr.sort()

for i in arr:
    print(i)