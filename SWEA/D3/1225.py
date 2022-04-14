from collections import deque

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = deque(list(map(int, input().split())))
    
    cnt = 0
    
    while arr[-1]:
        cnt %= 5
        cnt += 1
        
        right = arr.popleft() - cnt
        if right > 0:
            arr.append(right)
        else:
            arr.append(0)
            
    print(f'#{tc}',*arr)