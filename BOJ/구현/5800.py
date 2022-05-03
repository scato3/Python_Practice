n = int(input())
flag = 0
for _ in range(n):
    flag += 1
    maxNum = 0   
    C = list(map(int, input().split()))
    A = C[1:]
    A.sort(reverse=True)
    for i in range(len(A) - 1):
        if A[i] - A[i+1] > maxNum:
            maxNum = A[i] - A[i+1]
    print('Class {}'.format(flag))
    print('Max {}, Min {}, Largest gap {}'.format(max(A), min(A), maxNum))