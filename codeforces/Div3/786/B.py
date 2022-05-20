t = int(input())
for _ in range(t):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v',
             'w', 'x', 'y', 'z']
    k = input()
    a = k[0]
    b = k[1]
    cnt = ord(a) - 96
    if a in alpha:
        alpha.remove(a)
    print(25 * (cnt - 1) + alpha.index(b) + 1)