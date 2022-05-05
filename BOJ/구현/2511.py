a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a == b:
    print(10, 10)
    print('D')
    
else:
    A , B = 0, 0 
    for i in range(10):
        if a[i] > b[i]:
            A += 3
            win = 'A'
        elif a[i] < b[i]:
            B += 3
            win = 'B'
        else:
            A += 1
            B += 1
    
    print(A, B)
    if A == B:
        print(win)
    elif A > B:
        print('A')
    elif A < B:
        print('B')
