n = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > 0 and b > 0 :
        q1 += 1
    if a > 0 and b < 0 :
        q4 += 1
    if a < 0 and b < 0 :
        q3 += 1
    if a < 0 and b > 0 :
        q2 += 1
    if a == 0 or b == 0 :
        axis += 1

print('Q1: {}'.format(q1))
print('Q2: {}'.format(q2))
print('Q3: {}'.format(q3))
print('Q4: {}'.format(q4))
print('AXIS: {}'.format(axis))