n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    A = a[0] + a[4]
    B = a[1] + a[5]
    C = a[2] + a[6]
    D = a[3] + a[7]
    
    if A < 1:
        A = 1
    if B < 1:
        B = 1
    if C < 0:
        C = 0
    
    print(A + 5 * B + 2 * C + 2 * D)
    