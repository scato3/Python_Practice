n = int(input())
arr = []
ans = [i for i in range(10001)] 

for _ in range(n):
    arr.append(int(input()))
    
for i in ans:
    if i >= 3 and i % 3 == 0:
        ans.remove(i)

for i in ans:
    if i % 10 == 3:
        ans.remove(i)

for i in range(n):
    print(ans[arr[i]])
