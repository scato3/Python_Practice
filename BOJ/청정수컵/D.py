n = int(input())
a = list(input())
b = list(input())
flag = 0
A = sorted(a)
B = sorted(b)

while True:
    if A == B:
        flag = 1
    else:
        flag = 0
        break
    
    if a[0] == b[0] and a[-1] == b[-1]:
        flag = 1
    else:
        flag = 0
        break
    aeiou = 'aeiou'
    
    a = [char for char in a if char not in aeiou]
    b = [char for char in b if char not in aeiou]

    if a == b:
        flag = 1
        break
    else:
        flag = 0
        break
    
if flag:
    print('YES')
else:
    print('NO')