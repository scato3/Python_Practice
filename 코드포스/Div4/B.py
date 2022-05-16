N = int(input())

for _ in range(N):
    res = []
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    
    for i in range(n):
        dic[a[i]] = dic.get(a[i], 0) + 1
        if dic[a[i]] == 3:
            print(a[i])
            break
    else:
        print(-1)