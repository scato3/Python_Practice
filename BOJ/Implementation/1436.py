n = int(input())
check = 666
cnt = 0

while True:
    if '666' in str(check):
        cnt += 1
    if cnt == n:
        print(check)
        break 
    check += 1
    