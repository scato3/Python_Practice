import sys

n = int(sys.stdin.readline())
arr = set()

for _ in range(n):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == 'all':
            arr = set([i for i in range(1, 21)])
        else:
            arr = set()
    else:
        k, x = temp[0], temp[1]
        x = int(x)
        
        if k == 'add':
            arr.add(x)
        elif k == 'remove':
            arr.discard(x)
        elif k == 'check':
            if x in arr:
                print(1)
            else:
                print(0)
        elif k == 'toggle':
            if x in arr:
                arr.discard(x)
            else:
                arr.add(x)
                