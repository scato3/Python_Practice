s = list(input())
t = list(input())
flag = 0

def sol(t):
    global flag
    if len(s) == len(t):
        if s == t:
            flag = 1
        return
    
    if t[0] == 'B':
        t = t[::-1]
        t.pop()
        sol(t)
        t.append('B')
        t = t[::-1]
    
    if t[-1] == 'A':
        t.pop()
        sol(t)
        t.append('A')

sol(t)

if flag:
    print(1)
else:
    print(0)
        