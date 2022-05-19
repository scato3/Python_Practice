from collections import deque
n = int(input())
arr = deque()
for i in range(1, n+1):
    arr.append(i)

while True:
    if len(arr) == 1:
        print(*arr)
        break
    else:
        arr.popleft()
        x = arr.popleft()
        arr.append(x)

