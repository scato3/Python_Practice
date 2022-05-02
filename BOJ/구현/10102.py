n = int(input())
k = list(input())

if k.count('A') > k.count('B'):
    print('A')
elif k.count('A') < k.count('B'):
    print('B')
else:
    print('Tie')