n = int(input()) # 공간의 크기
x, y = 1, 1 # 시작점의 좌표
plans = input().split() # R R R U D D 

dx = [0, 0, -1, 1] # L R U D 를 했을 때 움직이는 X좌표를 배열로 설정
dy = [-1, 1, 0, 0] # L R U D 를 했을 때 움직이는 Y좌표를 배열로 설정
move_types = ['L','R','U','D'] # L R U D를 배열에 설정

for plan in plans: # plans를 다 돌면서 움직인다.
    for i in range(len(move_types)):
        if plan == move_types[i]: # plans의 값과 move_types를 비교한다.
            nx = x + dx[i] # x를 움직이고~
            ny = y + dy[i] # y를 움직이고~
    if nx < 1 or ny < 1 or nx > n or nx > ny: # 공간 밖으로 나가버리면 무시해버리기
        continue
    
    x, y = nx, ny # x, y값에 nx, ny를 넣는다.

print(x, y)