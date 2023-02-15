test_case = int(input())
for tc in range(test_case):
    stack = []
    values = input().split()
    for value in values:
        if value.isdecimal():
            stack.append(value)
        else:
            if value == '.':
                break
            elif len(stack) <= 1 and value.isdecimal() == False:
                if stack:
                    stack[0] = 'error'
                    break
                else:
                    stack.append('error')
                    break
            elif value == '*':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(int(v1)*int(v2)))
            elif value == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(int(v2)/int(v1)))
            elif value == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v1)+int(v2))
            elif value == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2)-int(v1))

    if len(stack) == 1:
        print(f'#{tc+1} {stack[0]}')
    else:
        print(f'#{tc + 1} error')
