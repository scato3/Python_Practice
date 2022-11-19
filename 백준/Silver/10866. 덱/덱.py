from collections import deque
import sys

arr = deque([])

for _ in range(int(input())):
    com = sys.stdin.readline().split()
    if com[0] == 'push_front':
        arr.appendleft(com[1])
    if com[0] == 'push_back':
        arr.append(com[1])
    if com[0] == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    if com[0] == 'pop_back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    if com[0] == 'size':
        print(len(arr))
    if com[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    if com[0] == 'front':
        if(len(arr)) == 0:
            print(-1)
        else:
            print(arr[0])
    if com[0] == 'back':
        if(len(arr)) == 0:
            print(-1)
        else:
            print(arr[-1])



