t = input()
n = len(t)

arr = []

for i in range(1, n+1):
    if n % i == 0:
        arr.append(i)
        
if len(arr) % 2 == 0:
    R = arr[len(arr) // 2 - 1]
    C = arr[len(arr) // 2]
else:
    R = C = arr[len(arr) // 2]
    
ans = []
idx = 0

for i in range(C):
    col = [0] * R
    for j in range(R):
        col[j] = t[idx]
        idx += 1
    ans.append(col)

for i in range(R):
    for j in range(C):
        print(ans[j][i], end = '')