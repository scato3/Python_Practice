from itertools import combinations_with_replacement

arr = [1, 5, 10, 50]
n = int(input())
result = []

for temp in combinations_with_replacement(range(4), n):
    sum = 0
    for i in temp:
        sum += arr[i]
    result.append(sum)

print(len(set(result)))


