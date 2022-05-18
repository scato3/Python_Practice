a = list(map(int, input().split()))
b = list(map(int, input().split()))

awin = 0
bwin = 0
draw = 0
for i in range(10):
    if a[i] > b[i]:
        awin += 1
    if a[i] < b[i]:
        bwin += 1
    if a[i] == b[i]:
        draw += 0

if awin == bwin:
    print('D')
if awin > bwin:
    print('A')
if awin < bwin:
    print('B')