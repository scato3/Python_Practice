n = int(input())
ans = 1
maxsum = 0

while ans * (ans +1) / 2 < n:
    ans += 1
    
print(ans - 1)