a = 2000
b = 2000

for i in range(3):
    c = int(input())
    a = min(a, c)

for i in range(2):
    d = int(input())
    b = min(b, d)
    
print(a + b - 50)