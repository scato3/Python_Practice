arr = []

for _ in range(9):
    arr.append(int(input()))

arr.sort()

temp1, temp2 = 0, 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if sum(arr) - arr[i] - arr[j] == 100:
            temp1 = arr[i]
            temp2 = arr[j]

arr.remove(temp1)
arr.remove(temp2)

for i in arr:
    print(i)