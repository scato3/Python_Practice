from collections import deque
import sys
n = int(sys.stdin.readline())
arr = deque()


for _ in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        arr.append(a[1])
    elif a[0] == 'pop':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(arr))
    elif a[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)
