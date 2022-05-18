n = int(input())

stack = []

for _ in range(n):
    stack.append(int(input()))
    
result = 1

Max = stack[-1]

for i in range(len(stack) - 1, -1, -1):
    if stack[i] > Max:
        Max = stack[i]
        result += 1

print(result)