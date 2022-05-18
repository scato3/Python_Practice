N, K = map(int, input().split())
check = [0] * (N+1)

cnt = 0
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if check[j] == 0:
            check[j] = 1
            cnt += 1
            if cnt == K:
                print(j)
                break