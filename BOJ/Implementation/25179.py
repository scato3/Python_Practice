n, m = map(int, input().split())
key = n - 1

if key % (m + 1) == 0:
    print("Can't win")
else:
    print("Can win")