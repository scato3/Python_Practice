t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if arr.count(min(arr)) == n:
        print(0)
    else:
        sum = 0
        for i in arr:
            if i != min(arr):
                sum += i - min(arr)
        print(sum)