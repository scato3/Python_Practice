arr = []

for _ in range(10):
    arr.append(int(input()))
    
score = 0

for i in arr:
    score += i
    if score > 100:
        if score - 100 > 100 - (score - i):
            score -= i
            break

print(score)