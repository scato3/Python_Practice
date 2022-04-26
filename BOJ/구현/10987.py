a = input()
str = 'aeiou'
ans = 0

for i in str:
    ans += a.count(i)
    
print(ans)