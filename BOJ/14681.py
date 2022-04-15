x = int(input())
y = int(input())

result = 0

if x > 0 and y > 0:
    result = 1
if x < 0 and y > 0:
    result = 2
if x < 0 and y < 0:
    result = 3
if x > 0 and y < 0:
    result = 4

print(result)