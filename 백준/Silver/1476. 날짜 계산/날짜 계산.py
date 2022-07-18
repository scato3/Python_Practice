A, B, C, cnt = 1, 1, 1, 1
a, b, c = map(int, input().split())

while True:
    if A == a and B == b and C == c:
        break
    A += 1
    B += 1
    C += 1
    cnt += 1
    if A >= 16:
        A -= 15
    if B >= 29:
        B -= 28
    if C >= 20:
        C -= 19

print(cnt)

