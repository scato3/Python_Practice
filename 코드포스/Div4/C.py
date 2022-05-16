N = int(input())

for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(n):
        if a[i % 2] % 2 != a[i] % 2:
            print('NO')
            break
    else:
        print('YES')