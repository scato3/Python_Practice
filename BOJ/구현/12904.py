s = list(input())
t = list(input())

while True:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if t == s:
        print(1)
        break
    if len(t) == 0:
        print(0)
        break