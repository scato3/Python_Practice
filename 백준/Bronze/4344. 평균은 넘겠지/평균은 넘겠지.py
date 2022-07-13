n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    tmp = 0
    for k in arr[1:]:
        if k > avg:
            tmp += 1
    per = tmp / arr[0] * 100
    print(f'{per:.3f}%')
