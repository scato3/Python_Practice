n, m = map(int, input().split())

if n == 1: # 1이면 이동할 공간이 없으니까 1
    print(1)
elif n == 2: # 세로가 2면 위 아래 1씩을 밖에 못 움직이니까 최대치인 4와, 가로 길이에 대한 값을 비교해서 최소값 출력
    print(min(4, (m - 1) // 2 + 1))
elif m <= 6: # 6이하라는 것은 4개의 이동 가능한 것을 다 쓰지 못한다는 것이니까 최대치인 4와 m
    print(min(4, m))
else: # 세로는 3이상, 가로는 7 이상이면 m - 2출력
    print(m - 2)