import sys
from collections import Counter		# ** Counter 사용시 import 해줘야 함
input = sys.stdin.readline

n = input().rstrip()
card = list(map(int, input().split()))		# 상근이 카드
m = input().rstrip()
test = list(map(int, input().split()))		# 비교하고싶은 숫자

cnt = Counter(card)     # Counter({10:3, 3:2, -10:2, 7:1, 6:1, 2:1})

for i in test:						# 비교하고 싶은 숫자가
    if i in cnt:					# cnt에 있으면
        print(cnt[i], end=" ")
    else:
        print(0, end=" ")