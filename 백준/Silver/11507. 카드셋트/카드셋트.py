s = input()
list = []

for i in range(0, len(s) - 2, 3):
    list.append(s[i:i + 3])

if len(set(list)) != len(list):
    print('GRESKA')
else:
    answer = {'P': 13, 'K': 13, 'H': 13, 'T': 13}
    for l in list:
        card_shape = l[0]
        answer[card_shape] -= 1
    for i in answer:
        print(answer[i],end=' ')

