alpha = [0] * 26
word = input().upper()
for i in word:
    alpha[ord(i) - 65] += 1

tmp = 0
first = max(alpha)
for i in alpha:
    if i == first:
        tmp += 1

if tmp >= 2:
    print('?')
else:
    print(chr(65 + alpha.index(first)))

