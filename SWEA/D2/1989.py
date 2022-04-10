T = int(input())

for tc in range(1, T+1):
    word = input()
    print('#{} {}'.format(tc, int(word == word[::-1])))