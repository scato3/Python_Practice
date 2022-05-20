from itertools import permutations
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = list(permutations(n, 3))

N = int(input())
for _ in range(N):
    balls, s, b = map(int, input().split())
    balls = list(str(balls))
    removed = 0
    for i in range(len(lst)):
        s_cnt, b_cnt = 0, 0
        i -= removed
        for j in range(3):
            balls[j] = int(balls[j])

            if balls[j] in lst[i]:
                if j == lst[i].index(balls[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            lst.remove(lst[i])
            removed += 1

print(len(lst))

