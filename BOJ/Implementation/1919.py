a = [0] * 26
b = [0] * 26

for i in input():
    a[ord(i) - 97] += 1
for i in input():
    b[ord(i) - 97] += 1
ans = 0
for i in range(26):
    ans += abs(b[i] - a[i])

print(ans)