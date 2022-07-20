n = int(input())
arr = []

for i in range(n):
    k = int(input())
    if k != 0:
        arr.append(k)
    else:
        arr.pop()

print(sum(arr))