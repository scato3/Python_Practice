t = int(input())
import math
cnt = 0
for tc in range(1, t+1):
    n, d = map(int, input().split())
    cnt += 1
    
    ans = math.ceil(n / (d * 2 + 1))
    print('#{} {}'.format(cnt, ans))