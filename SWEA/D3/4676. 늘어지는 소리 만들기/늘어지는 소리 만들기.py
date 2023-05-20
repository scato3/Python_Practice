t = int(input())

for tc in range(1, t+1):
    word = list(input())
    h = int(input())
    num = list(map(int, input().split()))
    num.sort(reverse=True)

    for i in num:
        word.insert(i, '-')

    print('#{}'.format(tc),end=' ')
    print(''.join(map(str, word)))