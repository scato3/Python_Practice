t = int(input())

for _ in range(t):
    n = int(input())
    maxNum = 0
    maxName = ''
    for _ in range(n):
        a, b = input().split()
        b = int(b)
        if b > maxNum:
            maxNum = b
            maxName = a
    print(maxName)
            