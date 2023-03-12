sentence = input()
target = str(input())
stack = ''

for w in sentence:
    stack += w
    if target in stack:
        stack.replace(target,'')

if stack:
    print(stack)
else:
    print('FRULA')