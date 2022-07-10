tmp = [0] * 26
arr = input()

for i in arr:
    tmp[ord(i) - 97] += 1

print(*tmp)