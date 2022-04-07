input_data = input() # 입력 데이터 받기
row = int(input_data[1]) # 행의 값은 뒤에 ex) 'a1' 처럼 [1]에 있다.
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 앞의 문자를 아스키코드로 바꿔서 제일 작은 값인 a를 빼고 +1을 하여 위치 파악

steps = [(-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1)] # 움직일 수 있는 거리에 대한 배열

result = 0

for step in steps:
    next_row = row + step[0] # steps를 돌면서 기존 row + step[0]에 들어있는 값을 넣어준다
    next_column = column + step[1] # steps를 돌면서 column + step[1] 값을 넣어준다.
    
    if next_row >= 1 and next_column >=1 and next_row <= 8 and next_column <= 8 : # 움직이고 나서의 값이 체스판 안에 있으면 통과
        result += 1
        
print(result)
        