arr = []
for i in range(9):
    arr.append(int(input()))

arr.sort()
for i in range(9):
    for j in range(i+1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            temp1 = arr[i]
            temp2 = arr[j]
arr.remove(temp1)
arr.remove(temp2)

for i in arr:
    print(i)