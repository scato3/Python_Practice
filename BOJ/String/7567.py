s = input()
count = 0

for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        count += 1

if len(s) - 1 == count:
    print((count * 5) + 10)

else:
    print(((count * 5) + 10) + (len(s) - count - 1) * 10)
        