maxsum = []
for _ in range(5):
    a = int(input())
    if a >= 40:
        maxsum.append(a)
    else:
        maxsum.append(40)

print(sum(maxsum) // 5)