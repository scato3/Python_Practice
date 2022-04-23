ans = ''
flag = 0
word = ''

a = input()

for i in a:
    if i == '<':
        flag = 1
        ans += word[::-1]
        word = ''
        ans += i
        continue
    elif i == ' ':
        ans += word[::-1]
        word = ''
        continue
    