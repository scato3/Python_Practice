arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
tmp = 0
for i in range(len(a)):
    for j in arr:
        if a[i] in j:
            tmp += arr.index(j) + 3
print(tmp)
