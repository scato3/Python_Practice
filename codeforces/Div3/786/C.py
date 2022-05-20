t = int(input())

for _ in range(t):
    s = input()
    t = input()
    n = len(s)

    if 'a' not in t:
        print(2 ** n)
    else:
        if t == 'a':
            print(1)
        else:
            print(-1)
