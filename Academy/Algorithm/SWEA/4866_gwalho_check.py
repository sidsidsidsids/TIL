test_case = int(input())
for tc in range(test_case):
    sentence = list(map(str,input()))

    starter = ['(','{','[']
    ender = [')', '}', ']']
    stack = []

    for i in sentence:
        if i in starter:
            stack.append(i)
        elif i in ender:
            if len(stack) != 0 and i == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) != 0 and i == '}' and stack[-1] == '{':
                stack.pop()
            elif len(stack) != 0 and i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc + 1} 0')
