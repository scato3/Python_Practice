n = int(input())
res = n
for _ in range(n):
    a = input()
    
    for i in range(len(a) - 2):
        if a[i] == a[i+1]:
            pass
        else:
            if a[i] in a[i+2:]:
                res -= 1
                break

print(res)