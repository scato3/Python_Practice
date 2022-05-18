N = int(input())

for _ in range(N):
    n = int(input())
    max = 0
    name = ''
    for _ in range(n):
        a, b = input().split()
        a = int(a)
        if a > max:
            max = a
            name = b
    
    print(name)