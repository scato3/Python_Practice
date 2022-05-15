n, m = map(int, input().split())
key = n - 1
check = [0] * (m + 1)
flag = 0
i = 0
sum = 0 
while True:
    flag = 1
    i += 1
    sum += i
    for j in range(i):
        check[j] = 1
        