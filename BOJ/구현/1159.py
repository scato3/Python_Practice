li = []
for _ in range(int(input())):
    li.append(input()[0])
    
s = set(li)
res = []

for i in s:
    if li.count(i) >= 5:
        res.append(i)

if len(res) == 0:
    print('PREDAJA')
else:
    print(''.join(sorted(res)))