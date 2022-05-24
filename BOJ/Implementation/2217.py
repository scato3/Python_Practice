def sol():
    ans = 0
    arr.sort(reverse=True)
    for i in range(t):
        arr[i] = arr[i] * (i + 1)
    return max(arr)

t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))

print(sol())
