n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    A = [a.count(4), a.count(3), a.count(2), a.count(1)]
    B = [b.count(4), b.count(3), b.count(2), b.count(1)]
    
    if A[0] > B[0]:
        print('A')
    elif A[0] < B[0]:
        print('B')
    elif A[1] > B[1]:
        print('A')
    elif A[1] < B[1]:
        print('B')
    elif A[2] > B[2]:
        print('A')
    elif A[2] < B[2]:
        print('B')
    elif A[3] > B[3]:
        print('A')
    elif A[3] < B[3]:
        print('B')
    else:
        print('D')
