c = [[0] * 15 for _ in range(5)]

for i in range(5):
    a = list(input())
    length = len(a)
    
    for j in range(length):
        c[i][j] = a[j]

for i in range(15):
    for j in range(5):
        if c[j][i] == 0:
            continue
        else:
            print(c[j][i], end='')
    