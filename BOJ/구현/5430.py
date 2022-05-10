from collections import deque

T = int(input())

for _ in range(T):
    cmd = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    q = deque(arr)
    flag = 0
    
    if n == 0:
        q = []
    
    for i in cmd:
        if i == 'R':
            flag += 1
        if i == 'D':
            if len(q) == 0:
                print('error')
                break
            elif flag % 2 == 0:
                q.popleft()
            else:
                q.pop()
    else:
        if flag % 2 == 0:
            print('[' + ','.join(q) + ']')
        else:
            q.reverse()
            print('[' + ','.join(q) + ']')