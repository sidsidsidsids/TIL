sentence = []
while True:
    t = input()
    sentence.append(t)
    if t == '.':
        break

opener = ['(','[']
closer = [')',']']
for i in range(len(sentence) - 1):
    stack = []
    for w in sentence[i]:
        if w in opener:
            stack.append(w)
        elif w in closer:
            if stack and stack[-1] == '(' and w == ')':
                stack.pop()
            elif stack and stack[-1] == '[' and w == ']':
                stack.pop()
            else:
                stack.append(w)
        else:
            pass
    if stack:
        print('no')
    else:
        print('yes')
