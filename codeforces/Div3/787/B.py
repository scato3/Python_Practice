t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(n-2, -1, -1):
        while arr[i] >= arr[i+1]:
            cnt += 1
            arr[i] = arr[i] // 2
            if arr[i] == 0:
                break
        if arr[i] == arr[i+1]:
            cnt = -1
            break
    print(cnt)

