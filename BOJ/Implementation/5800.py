n = int(input())
cnt = 0
for _ in range(n):
    cnt += 1
    print('Class {}'.format(cnt))
    arr = list(map(int, input().split()))
    arr.remove(arr[0])
    arr.sort(reverse=True)
    ans = 0
    for i in range(len(arr) - 1):
        if arr[i] - arr[i+1] > ans:
            ans = arr[i] - arr[i+1]
    print('Max {}, Min {}, Largest gap {}'.format(max(arr), min(arr), ans))