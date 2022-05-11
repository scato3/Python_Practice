n = int(input())

arr = list(map(int, input().split()))

b, c = map(int, input().split())

sum = 0

for i in range(n):
    if arr[i] > 0:
        arr[i] -= b
        sum += 1
    
    if arr[i] > 0:
        sum += (arr[i] // c)
        
        if arr[i] % c != 0:
            sum += 1

print(sum)