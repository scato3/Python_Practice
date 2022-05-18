def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1

ans = []
while True:
    n = int(input())
    if n == 0:
        break
    
    cnt = 0
    for i in range(n+1, 2*n+1):
        if isPrime(i) == 1:
            cnt += 1
    ans.append(cnt)

for i in ans:
    print(i)