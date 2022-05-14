n = int(input())
result = n

for i in range(n):
    a = input()
    for j in range(len(a) - 1):
        if a[j] == a[j+1]:
            pass 
        else:
            if a[j] in a[j+1:]:
                result -= 1
                break;
print(result)