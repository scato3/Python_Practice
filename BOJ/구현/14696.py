n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    
    listA = [a.count(4), a.count(3), a.count(2), a.count(1)]
    listB = [b.count(4), b.count(3), b.count(2), b.count(1)]
    
    if listA[0] > listB[0]:
        print('A')
    elif listA[0] < listB[0]:
        print('B')
    elif listA[1] > listB[1]:
        print('A')
    elif listA[1] < listB[1]:
        print('B')
    elif listA[2] > listB[2]:
            print('A')
    elif listA[2] < listB[2]:
        print('B')
    elif listA[3] > listB[3]:
            print('A')
    elif listA[3] < listB[3]:
        print('B') 
    else:
        print('D')