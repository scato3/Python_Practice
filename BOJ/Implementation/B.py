from re import A


n = int(input())
arr = list()
arr2 = set()
for _ in range(n):
    arr.append(input())
    
cnt = 0
for i in arr[1:]:
    if i not in arr2 and i != 'ENTER':
        cnt += 1      
    arr2.add(i)   
    if i == 'ENTER':
        arr2 = set()

print(cnt)