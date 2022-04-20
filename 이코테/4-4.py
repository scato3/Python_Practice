n, m = map(int, input().split()) # 공백으로 구분하여 데이터 받기

d = [[0] * m for _ in range(n)] # 방문한 위치를 구분하기 위하여 다 0으로 초기화

x, y, direction = map(int, input().split()) # 현재 위치를 받아옴
d[x][y] = 1 # 현재 위치를 방문 처리한다.

array = []
for i in range(n):
    array.append(list(map(int, input().split()))) # 맵 전체 정보를 공백으로 구분하여 받아온다.
    
dx = [-1, 0, 1, 0] # 북, 동, 남, 서에 대한 처리
dy = [0, 1, 0, -1] 

def turn_left(): # 왼쪽으로 회전하는 함수 정의
    global direction # 전역변수 direction을 가져다 쓴다.
    direction -= 1 # 왼쪽으로 돌고
    if direction == -1: 
        direction = 3 # 만약 북에서 왼쪽으로 돌아서 -1이 된다면 3으로 바꿔준다.
        
count = 1
turn_time = 0 
while True:
    # 왼쪽으로 돌고
    turn_left() 
    nx = x + dx[direction] # x의 좌표
    ny = y + dy[direction] # y의 좌표
    
    if d[nx][ny] == 0 and array[nx][ny] == 0: # 회전하고 나서의 값이 가보지 않거나, 육지일 경우
        d[nx][ny] = 1
        x = nx # 현재 위치 수정
        y = ny
        count += 1 
        turn_time = 0
        continue
    
    else:
        turn_time += 1 # 갈 수 없으면 돈다.
        
    if turn_time == 4: # 네 방향 모두 갈 수 없으면
        nx = x - dx[direction]
        ny = y - dy[direction]
          
        if array[nx][ny] == 0: # 뒤로 갈 수 있다면 돌아가기
            x = nx
            y = ny           
        else:
            break
        turn_time = 0

print(count)