people = 0
arr = []
for _ in range(10):
    a, b = map(int, input().split())
    people += b
    people -= a
    arr.append(people)

print(max(arr))