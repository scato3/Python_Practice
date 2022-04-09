T = int(input())

for i in range(1, T+1):
    num = int(input())
    price = list(map(int, input().split()))
    
    last = price[-1]
    cnt = 0
    
    for j in range(num - 1, -1, -1):
        if price[j] > last:
            last = price[j]
        cnt += last - price[j]
    print("#{} {}".format(i, cnt))