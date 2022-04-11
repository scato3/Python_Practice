T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M:
        N, M = M, N
        A, B = B, A
    max_sum = 0
    
    for i in range(M-N+1):
        temp = 0
        for j in range(N):
            temp += A[j] * B[i+j]
        if temp > max_sum:
            max_sum = temp
    print('#{} {}'.format(tc, max_sum))