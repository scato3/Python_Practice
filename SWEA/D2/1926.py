T = int(input())

for i in range(1, T+1):
    s = sum(1 for x in str(i) if x in ['3', '6', '9']) # i를 str로 바꿔서 그 값이 3, 6, 9에 있으면 1을 더해준다. 2개면 2를 더해~
    
    if s == 0:
        print(i, end= ' ')
    else:
        print('-'*s, end= ' ') # s의 숫자만큼 -를 출력