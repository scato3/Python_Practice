text = [input() for _ in range(5)]
max_length = 0

for i in range(5):
    if len(text[i]) > max_length:
        max_length = len(text[i])
        
for i in range(max_length):
    for j in range(5):
        if i < len(text[j]):
            print(text[j][i], end = '')
        