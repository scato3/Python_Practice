ans = ''
stack = ''
tag = False

for i in input():
    if i == '<':
        tag = True
        ans += stack[::-1]
        stack = ''
        ans += i
        continue
    elif i == '>':
        tag = False
        ans += i
        continue
    elif i == ' ':
        ans += stack[::-1] + ' '
        stack = ''
        continue

    if tag == True:
        ans += i
    else:
        stack += i

print(ans + stack[::-1])