num = {'0001101':0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in range(N):
        if sum(map(int, arr[i])) == 0:
            continue
        else:
            v_code = arr[i]
            for j in range(M-1, -1, -1):
                if v_code[j] == '1':
                    my_code = v_code[j-55:j+1]
                    break
            break
    my_code_value = [num[my_code[i:i+7]] for i in range(0, 56, 7)] # 딕셔너리기 때문에 기분 좋게 my_code_value 값이 스르륵 들어간다.
    
    odd = 0
    even = 0
    for i in range(7):
        if i % 2 == 0:
            even += my_code_value[i]
        else:
            odd += my_code_value[i]
    result = even * 3 + odd + my_code_value[-1]
    
    if result % 10 == 0:
        print('#{} {}'.format(tc, sum(my_code_value)))
    else:
        print('#{} {}'.format(tc, 0))