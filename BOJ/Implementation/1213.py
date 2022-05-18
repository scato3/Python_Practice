name = input()
cnt = [0 for _ in range(26)]

for i in name:
    cnt[ord(i) - 65] += 1

odd = 0
oddName = ''
alpha = ''

for i in range(26):
    if cnt[i] % 2 == 1:
        odd += 1
        oddName += chr(i+65)
    alpha += chr(i+65) * (cnt[i] // 2)
    
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha + oddName + alpha[::-1])