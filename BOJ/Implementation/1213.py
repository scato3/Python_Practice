a = input()
names = [0] * 26
for i in a:
    names[ord(i) - 65] += 1

odd = 0
oddname = ''
even = ''

for i in range(26):
    if names[i] % 2 == 1:
        odd += 1
        oddname = chr(i + 65)
    even += chr(i + 65) * (names[i] // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(even + oddname + even[::-1])