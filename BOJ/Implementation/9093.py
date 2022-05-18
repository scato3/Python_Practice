T = int(input())

for _ in range(T):
    a = input().split()
    
    for i in range(len(a)):
        if len(a[i]) != 1:
            a[i] = a[i][::-1]
    
    print(' '.join(a))