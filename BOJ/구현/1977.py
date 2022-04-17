m = int(input())
n = int(input())
arr = []
i = 1
while i ** 2 <= n:
    if m <= i ** 2 <= n:
        arr.append(i ** 2)
    i += 1

if len(arr) == 0:
    print(-1) 
else:
    print(sum(arr))
    print(min(arr))