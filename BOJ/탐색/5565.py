n = int(input())
book = []

for _ in range(9):
    book.append(int(input()))
    
print(n - sum(book))