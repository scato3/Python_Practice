while True:
    a = input()
    if a == '.':
        break
    stack = []
    tmp = 1
    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                tmp = 0
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                tmp = 0
                break
            elif stack[-1] == '[':
                stack.pop()
    if tmp == 1 and not stack:
        print('yes')
    else:
        print('no')
