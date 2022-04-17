n = int(input())
arr = []
for i in range(1, n+1):
    arr.append(int(input()))
    
arr.sort()

for i in range(len(arr)):
    print(arr[i])