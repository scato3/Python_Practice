T = 10

for tc in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))
    max_sum = 0
    
    for i in range(2, N-2):
        def_1 = building[i] - building[i-1]
        def_2 = building[i] - building[i-2]
        def1 = building[i] - building[i+1]
        def2 = building[i] - building[i+2]
        
        if def_1 > 0 and def_2 > 0 and def1 > 0 and def2 > 0:
            max_sum += min(def1, def2, def_1, def_2)
    print('#{} {}'.format(tc, max_sum))