n = int(input())
arr = []
for _ in range(n):
    k = int(input())
    arr.append(k)
    num = 1
    while True:
        if k == 1:
            print(1, 1)
            break
        else:
            if num ** 2 < k <= (num+1) ** 2:
                if k < (num + 1) ** 2 - num:
                    print(num + 1 - (((num + 1) ** 2 - num) - k), num + 1)
                    break
                elif k == (num+1) ** 2 - num:
                    print(num + 1, num + 1)
                    break
                else:
                    print(num + 1, num + 1 - (k - ((num + 1) ** 2 - num)))
                    break
        num += 1
                