ans = ''
word = ''
flag = 0

for i in input():
    if i == '<':
        flag = 1
        ans += word[::-1]
        word = ''
        ans += i
        continue
    elif i == '>':
        flag = 0
        ans += i
        continue
    elif i == ' ':
        ans += word[::-1] + ' '
        word = ''
        continue
    if flag:
        ans += i
    else:
        word += i

