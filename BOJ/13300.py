n, k = map(int, input().split())

boy = [0] * 1000
girl = [0] * 1000

for i in range(n):
    s, age = map(int, input().split())
    
    if s == 0:
        girl[age] += 1
    else:
        boy[age] += 1

for i in range(1, 7):
    if girl[i] % k == 0:
        girl[i] = girl[i] // k
    else:
        girl[i] = (girl[i] // k) + 1
    if boy[i] % k == 0: 
        boy[i] = boy[i] // k
    else:
        boy[i] = (boy[i] // k) + 1

print(sum(girl) + sum(boy))