n = input()

a = 0
b = 0

k = len(n) // 2

for i in n[:k]:
    a += int(i)

for i in n[k:]:
    b += int(i)

if a == b:
    print('LUCKY')
else:
    print('READY')