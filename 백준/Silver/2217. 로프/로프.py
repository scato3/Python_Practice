n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(n):
    arr[i] = arr[i] * (i + 1)

print(max(arr))