numbers = int(input())
stack = []
for _ in range(numbers):
    numeric = int(input())
    if numeric:
        stack.append(numeric)
    else:
        stack.pop()
print(sum(stack))