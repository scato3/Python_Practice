n = int(input())

for _ in range(n):
    k = input()
    
    if (int(k[0]) + int(k[1]) + int(k[2])) == (int(k[3]) + int(k[4]) + int(k[5])):
        print('YES')
    else:
        print('NO')