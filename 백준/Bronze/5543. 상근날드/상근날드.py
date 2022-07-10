tmp1 = 2001
tmp2 = 2001
for i in range(3):
    a = int(input())
    if tmp1 > a:
        tmp1 = a

for i in range(2):
    b = int(input())
    if tmp2 > b:
        tmp2 = b

print(tmp1 + tmp2 - 50)


