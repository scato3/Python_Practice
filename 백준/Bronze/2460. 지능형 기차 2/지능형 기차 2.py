sum = 0
people = []

for i in range(10):
    a, b = map(int, input().split())
    sum += b - a
    people.append(sum)
    
print(max(people))