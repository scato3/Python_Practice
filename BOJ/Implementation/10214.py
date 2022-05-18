n = int(input())

for _ in range(n):
    A = []
    B = []
    
    for _ in range(9):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    if sum(A) > sum(B):
        print('Yonsei')
    elif sum(A) == sum(B):
        print('Draw')
    else:
        print('Korea')