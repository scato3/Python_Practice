T = 10

for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    
    for _ in range(N):
        max_idx = box.index(max(box))
        min_idx = box.index(min(box))
        
        box[max_idx] -= 1
        box[min_idx] += 1
        
    result = max(box) - min(box)
    if result < 2:
        break
    print('#{} {}'.format(tc, result))
    
    