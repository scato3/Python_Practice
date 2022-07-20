from collections import deque
n, k = map(int, input().split())
arr = deque()
for i in range(1, n+1):
    arr.append(i)
ans = []
print('<',end='')
while True:
    if not arr:
        break
    for i in range(k-1):
        tmp = arr.popleft()
        arr.append(tmp)
    ans.append(arr.popleft())
print(', '.join(str(i) for i in ans), '>',sep='')





