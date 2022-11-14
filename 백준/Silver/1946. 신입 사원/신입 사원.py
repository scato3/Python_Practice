t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] * n
    for i in range(n):
        a, b = map(int, input().split())
        arr[i] = [a, b]

    sort_arr = sorted(arr, key = lambda x:x[0])
    ans = 1
    temp = sort_arr[0][1]
    for i in range(1, n):
        if sort_arr[i][1] < temp:
            temp = sort_arr[i][1]
            ans += 1
    print(ans)