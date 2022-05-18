n = int(input())
arr = list(map(int, input().split()))
temp = 0
sum = 0

for i in range(n):
    if arr[i] == 1:
       temp += arr[i]
       sum += temp
    else:
        temp = 0

print(sum)