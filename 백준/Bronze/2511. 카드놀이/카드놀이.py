a = list(map(int, input().split()))
b = list(map(int, input().split()))

suma = 0
sumb = 0
if a == b:
    print(10, 10)
    print('D')
else:
    for i in range(10):
        if a[i] > b[i] :
            suma += 3
            win = 'A'
        if a[i] < b[i] :
            sumb += 3
            win = 'B'
        if a[i] == b[i] :
            suma += 1
            sumb += 1
    
    print(suma, sumb)

    if suma == sumb:
        print(win)
    elif suma > sumb:
        print('A')
    elif suma < sumb:
        print('B')
    