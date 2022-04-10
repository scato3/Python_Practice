T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    res = 1
    for i in range(9):
        check_row = [0] * 10
        check_col = [0] * 10
        for j in range(9):
            row = arr[i][j]
            col = arr[j][i]
            if check_row[row]:
                res = 0
            if check_col[col]:
                res = 0
            check_row[row], check_col[col] = 1, 1

            if i % 3 == 0 and j % 3 == 0:
                check_box = [0] * 10
                for k in range(3):
                    for l in range(3):
                        box = arr[k+i][l+j]
                        if check_box[box]:
                            res = 0
                        check_box[box] = 1
                    
    print('#{} {}'.format(tc, res))