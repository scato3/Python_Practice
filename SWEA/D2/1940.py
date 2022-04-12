T = int(input())

for tc in range(1, T+1):
    N = int(input())
    speed = 0
    max_sum = 0
    for n in range(1, N+1):
        A = input().split()
        if A[0] == '1':
            speed += int(A[1])
            max_sum += speed
        if A[0] == '0':
            max_sum += speed
        if A[0] == '2':
            speed -= int(A[1])
            if speed < 0:
                speed = 0
            max_sum += speed
    print('#{} {}'.format(tc, max_sum))