T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [[0] * N for _ in range(N)] # 전체 범위를 설정
    for i in range(N):
        area[i] = list(map(int, input().split())) # 파리가 몇마리가 있는지 받아오기
        
die = [] # 죽은 파리에 대한 배열
    
for i in range(N-M+1): # 시작점에 대한 값, N-M+1 ~ M까지 후려치면 전체 범위를 다 커버칠 수 있다.
    for j in range(N-M+1):
        count = 0 # 범위 한바퀴를 돈 이후 초기화
        for k in range(M): # 파리를 후려치는 것을 완전탐색
                for l in range(M):
                    count += area[i+k][j+l]
                die.append(count)
print('#{} {}'.format(tc, max(die)))