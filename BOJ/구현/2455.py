people = 0
arr = []
for _ in range(4):
    a, b = map(int, input().split())
    people += b
    people -= a
    arr.append(people)

print(max(arr))