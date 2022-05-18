s = input()
arr = []

for i in s:
    arr.append(s)
    s = s[1:]
    
for i in sorted(arr):
    print(i)