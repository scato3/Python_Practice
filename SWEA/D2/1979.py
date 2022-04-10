T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    result = 0
    
    for i in range(N):
        count = 0
        for j in range(N): # 가로에 해당하는 부분
            if puzzle[i][j] == 1: # 1이면 count를 1 증가
                count += 1
            if puzzle[i][j] == 0 or j == N-1: # 0을 만나거나, 가로의 끝에 가버리면 count가 K와 같은지 판별
                if count == K:
                    result += 1
                count = 0 # count = 0 초기화
        for k in range(N): # 세로에 해당하는 부분
            if puzzle[k][i] == 1:
                count += 1
            if puzzle[k][i] == 0 or k == N-1:
                if count == K:
                    result += 1
                count = 0
    print('#{} {}'.format(tc, result))