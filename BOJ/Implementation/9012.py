t = int(input())

for _ in range(t):
    a = input()
    stack = []
    res = 'YES'
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(a[i])
        else:
            if len(stack) == 0:
                res = 'NO'
                break
            else:
                stack.pop()

    if len(stack) != 0:
        res = 'NO'

    print(res)