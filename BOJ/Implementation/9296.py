n = int(input())
cnt = 0
for _ in range(n):
    cnt += 1
    a, b = map(int, input().split())
    print('Case {}: {}'.format(cnt, a + b))