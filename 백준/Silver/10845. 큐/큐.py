from sys import stdin

n = int(stdin.readline())
stack = []
for i in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    if cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    if cmd[0] == 'size':
        print(len(stack))
    if cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if cmd[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    if cmd[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])