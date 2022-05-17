a = list(input())
a.sort(reverse=True)
sum = 0
if int(a[-1]) != 0:
    print(-1)
else:
    for i in a:
        sum += int(i)
    if sum % 3 == 0:
        for i in a:
            print(i,end='')
    else:
        print(-1)