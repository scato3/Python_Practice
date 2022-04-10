T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)] # 스도쿠 판 만들기
    res = 1 # result 기본값
    
    for i in range(9): # 가로에 대한 값
        check_row = [0] * 10 # 값이 중복되는지 확인할건데, arr값이 1~9가 들어가기 때문에 overflow를 방지하기 위해 +1
        check_col = [0] * 10
        for j in range(9): # 세로에 대한 값
            row = arr[i][j] 
            col = arr[j][i]
            if check_row[row]: # row를 index 삼아서 체크한 것이 있으면(중복되는 값이 있으면) res는 0
                res = 0
            if check_col[col]:
                res = 0
            check_row[row], check_col[col] = 1, 1 # 중복되는 값이 없다면 1, 1을 넣어준다.

            if i % 3 == 0 and j % 3 == 0: # i, j가 0, 3, 6일 경우(3짜리 미니 박스에 대한 것)
                check_box = [0] * 10 # 위와 똑같다
                for k in range(3): # 3x3에서의 가로
                    for l in range(3):
                        box = arr[k+i][j+l] # box가 k + i, j + l, 즉 0~2 + 0, 3, 6에 대한 값(3x3)
                        if check_box[box]: # box 값을 index 삼아 중복된 값이 있으면 res는 0
                            res = 0
                        check_box[box] = 1 # 없다면 1을 넣어준다.
    print('#{} {}'.format(tc, res))