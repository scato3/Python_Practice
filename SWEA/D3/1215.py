T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(8)]
    cnt = 0
    
    for i in range(8):
        for j in range(8-n+1):
            box1 = []
            for k in range(n):
                box1.append(arr[i][j+k])
            if box1 == box1[::-1]:
                cnt += 1
    for i in range(8-n+1):
        for j in range(8):
            box2 = []
            for k in range(n):
                box2.append(arr[i+k][j])
            if box2 == box2[::-1]:
                cnt += 1         
    print('#{} {}'.format(tc, cnt))