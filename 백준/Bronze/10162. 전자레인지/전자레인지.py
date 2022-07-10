num = int(input())

if num % 10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = num // 300
    b = (num % 300) // 60
    c = (num % 300) % 60 // 10
    print(a, b, c)
