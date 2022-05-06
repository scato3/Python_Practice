h1, m1, s1 = list(map(int, input().split(':')))
h2, m2, s2 = list(map(int, input().split(':')))

a = h2 - h1
b = m2 - m1
c = s2 - s1

if c < 0:
    c += 60
    b -= 1

if b < 0:
    b += 60
    a -= 1

if a < 0 :
    a += 24

print('%02d:%02d:%02d' %(int(a), int(b), int(c)))