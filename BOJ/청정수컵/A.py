n, m, k = map(int, input().split())

while True:
    if k <= 0:
        k += n
    elif (k + m - 3) % n == 0:
            print(n)
            break
    else:
        print((k + m - 3) % n)
        break