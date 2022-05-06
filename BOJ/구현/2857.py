arr = []
for i in range(1, 6):
    a = input()

    if 'FBI' in a:
        arr.append(i)
        
if len(arr) == 0:
    print('HE GOT AWAY!')
else:
    print(*arr)