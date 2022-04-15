n = int(input())

for tc in range(1, n+1):
    a, b = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(tc, a, b, a+b))