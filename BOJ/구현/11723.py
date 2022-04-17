import sys
input = lambda : sys.stdin.readline().strip()

m = int(input())
s = []

for _ in range(m):
    a = input().split()
    
    if a[0] == 'all':
        s.clear()
        s = [i for i in range(1, 21)]
        continue
    elif a[0] == 'empty':
        s.clear()
        continue
    
    n = int(a[1])
    if a[0] == 'add':
        if n not in s:
            s.append(n)
    elif a[0] == 'remove':
        if n in s:
            s.remove(n)
    elif a[0] == 'check':
        if n in s:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if n in s:
            s.remove(n)
        else:
            s.append(n)
        