dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
result = 0

for i in a:
    for j in dial:
        if i in j:
            result += dial.index(j) + 3

print(result)
