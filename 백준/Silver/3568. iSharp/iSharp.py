str = input()
str_list = str.split(' ')
basic = str_list[0]
del str_list[0]

for k in str_list:
    k = k.replace(',','').replace(';','')

    print(basic,end='')

    for i in range(len(k)-1, 0, -1):
        if not k[i].isalpha():
            if k[i] == ']':
                print('[',end='')
            elif k[i] == '[':
                print(']',end='')
            else:
                print(k[i],end='')
    print(' ',end='')

    for i in range(len(k)):
        if k[i].isalpha():
            print(k[i],end='')

    print(';')
