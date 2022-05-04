n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    even = []
    for i in range(7):
        if arr[i] % 2 == 0:
            even.append(arr[i])
    
    print(sum(even), min(even))
            