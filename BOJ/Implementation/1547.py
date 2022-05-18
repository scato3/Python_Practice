n = int(input())

cups = [1, 2, 3]
for _ in range(n):
    a, b = map(int, input().split())
    
    ai = cups.index(a)
    bi = cups.index(b)
    
    cups[ai], cups[bi] = cups[bi], cups[ai]

print(cups[0])