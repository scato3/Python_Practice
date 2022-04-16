str = input()
arr = [0] * 26

for i in str:
    arr[ord(i) - 97] += 1

print(*arr)