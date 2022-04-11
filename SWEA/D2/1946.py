T = int(input())

for tc in range(1, T+1):
    N = int(input())
    text = ''
    for n in range(N):
        a, b = input().split()
        text += a * int(b)
    print('#{}'.format(tc))
    for i in range(1, len(text), 10):
        print(text[i-1:i+10-1])