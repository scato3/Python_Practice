t = int(input())

for _ in range(t):
    arr = list(input())
    arr2 = []
    arr3 = []
    i = 0
    while True:
        if i >= len(arr) - 1:
            break
        if arr[i] == arr[i + 1]:
            arr2.append(i)
            arr2.append(i + 1)
            i += 2
        else:
            i += 1
    for i in range(len(arr)):
        if i not in arr2:
            arr3.append(arr[i])
    arr4 = ''
    for i in arr3:
        if arr3.count(i) % 2 == 0:
            arr4 = i
            break
    print(len(arr3) - arr3.count(arr4))