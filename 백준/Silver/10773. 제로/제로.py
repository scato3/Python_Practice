n = int(input())
arr = []

for _ in range(n):
    a = int(input())
    if a != 0:
        arr.append(a)
    else:
        arr.pop()

print(sum(arr))