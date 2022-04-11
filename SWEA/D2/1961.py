T = int(input())

def turn(a, N):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = a[N-1-j][i]
    return new_arr

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    turn_90 = turn(arr, N)
    turn_180 = turn(turn_90, N)
    turn_270 = turn(turn_180, N)
    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, turn_90[i])), end= ' ')
        print(''.join(map(str, turn_180[i])), end= ' ')
        print(''.join(map(str, turn_270[i])), end='')
        print()