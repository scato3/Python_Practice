from collections import deque
import sys

n = int(input())
arr = deque()
for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push_front':
        arr.appendleft(com[1])
    elif com[0] == 'push_back':
        arr.append(com[1])
    elif com[0] == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif com[0] == 'pop_back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif com[0] == 'size':
        print(len(arr))
    elif com[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif com[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])

