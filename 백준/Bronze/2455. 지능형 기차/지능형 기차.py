people = 0
peoples = []

for _ in range(4):
    off, on = map(int, input().split())
    people += on
    people -= off
    peoples.append(people)
    
print(max(peoples))