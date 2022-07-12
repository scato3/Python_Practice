t = int(input())

for i in range(t):
    num, s = input().split()
    num = int(num)
    text = ''
    for k in s:
        text += k * num
    print(text)
