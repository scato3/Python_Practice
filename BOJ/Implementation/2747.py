n = int(input())
arr = [0, 1]

for i in range(n-1):
    arr.append(arr[i] + arr[i+1])

print(arr[-1])