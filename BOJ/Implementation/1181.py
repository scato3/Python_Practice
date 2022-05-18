n = int(input())
arr = set()

for _ in range(n):
    arr.add(input())

arr = list(arr)
arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)