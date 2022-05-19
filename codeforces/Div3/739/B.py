t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    circle = abs(a - b) * 2 
    
    if a > circle or b > circle or c > circle:
        print(-1)
        continue
    else:
        if c > circle / 2:
            d = c - circle // 2
        else:
            d = c + circle // 2
    
    print(d)