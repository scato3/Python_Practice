def isPrime(n):
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                return 0
    else:
        return 0
    return 1

m = int(input())
n = int(input())
arr = []
for i in range(m, n+1):
    if isPrime(i) == 1:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
