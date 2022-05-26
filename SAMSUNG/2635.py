n = int(input())
max = []

for i in range(1, n+1):
    arr = [n]
    arr.append(i)

    idx = 1

    while True:
        next_num = arr[idx-1] - arr[idx]
        if next_num < 0:
            break
        arr.append(next_num)
        idx += 1

    if len(max) < len(arr):
        max = arr

print(len(max))
print(*max)
