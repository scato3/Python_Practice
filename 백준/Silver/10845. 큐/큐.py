import sys

n = int(input())
arr = []
for _ in range(n):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        arr.append(com[1])
    if com[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(0))
    if com[0] == 'size':
        print(len(arr))
    if com[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    if com[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    if com[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])