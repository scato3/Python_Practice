t = int(input())

for tc in range(1, t+1):
    cards = input()
    my_card = {
        'S': [],
        'D': [],
        'H': [],
        'C': []
    }
    print('#{}'.format(tc), end=' ')
    for i in range(0, len(cards), 3):
        c = cards[i]
        n = cards[i+1:i+3]

        if n not in my_card[c]:
            my_card[c].append(n)
        else:
            print('ERROR')
            break
    else:
        for key, value in my_card.items():
            print(13 - len(value),end=' ')
        print()
