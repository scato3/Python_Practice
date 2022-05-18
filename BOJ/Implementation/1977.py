n = int(input())
m = int(input())

i = 1
arr = []
while i ** 2 <= m:
    if n <= i ** 2:
        arr.append(i**2)
    i+= 1

if len(arr):
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
