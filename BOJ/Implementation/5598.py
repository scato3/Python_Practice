a = list(input())

for i in range(len(a)):
    k = ord(a[i]) - 3
    if k < ord('A'):
        k += 26
    a[i] = chr(k)
    
print(''.join(a))