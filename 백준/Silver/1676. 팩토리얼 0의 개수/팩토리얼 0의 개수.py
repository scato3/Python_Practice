import math
n = int(input())
num = math.factorial(n)
cnt = 0
for i in str(num)[::-1]:
    if i != '0':
        break
    else:
        cnt += 1
print(cnt)