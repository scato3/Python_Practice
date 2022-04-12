T = int(input())

for tc in range(1, T+1):
    n = int(input())
    compare = [0] * 101 # 1점부터 100점까지의 배열
    score = list(map(int, input().split()))
    max_sum = 0 # 빈도수 횟수에 대한 변수
    max_score = 0 # 가장 큰 숫자에 대한 변수
    for i in range(len(score)):
        compare[score[i]] += 1 # 값이 들어올 때의 점수를 인덱스 삼아 누적 시킨다.
    for x in range(1, len(compare)):
        if compare[x] >= max_sum: #compare[x]에 대한 값(빈도 수)에 따라서 max_sum을 갱신시킨다.
            max_sum = compare[x]
            max_score = x # 가장 큰 점수
    print('#{} {}'.format(tc, max_score))