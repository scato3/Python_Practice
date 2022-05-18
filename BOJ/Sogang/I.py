n = int(input())
a = input()
cnt = 0
for i in range(len(a) - 1):
    if ord(a[i]) == ord(a[i-1]) + 1 or ord(a[i]) == ord(a[i-1]) - 1:
        cnt += 1
    elif ord(a[i]) == ord(a[i+1]) + 1 or ord(a[i]) == ord(a[i+1]) - 1:
        cnt += 1
    
        
if cnt == 4:
    if ord(a[-1]) == ord(a[-2]) + 1 or ord(a[-1]) == ord(a[-2]) - 1:
        cnt += 1
        
if cnt >= 5:
    print('YES')
else:
    print('NO')