n = int(input())
arr = list(map(int, input().split()))

maxsum = 0
result = 0

for i in range(n):
    if arr[i] == 1:
        maxsum += 1
        result += maxsum
    else:
        maxsum = 0
        
print(result)